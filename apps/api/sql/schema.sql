-- Career AI Assistant Database Schema
-- PostgreSQL with pgvector extension for vector similarity search

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Documents table: stores metadata about source documents (KB files)
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    source_path VARCHAR(500) NOT NULL UNIQUE,
    course_id VARCHAR(10),
    module_id VARCHAR(10),
    file_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE INDEX idx_documents_course_id ON documents(course_id);
CREATE INDEX idx_documents_source_path ON documents(source_path);

-- Chunks table: stores chunked text from documents
CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    heading TEXT,
    heading_level INTEGER,
    chunk_index INTEGER,
    char_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE INDEX idx_chunks_document_id ON chunks(document_id);
CREATE INDEX idx_chunks_heading ON chunks(heading);

-- Embeddings table: stores vector embeddings for semantic search
CREATE TABLE IF NOT EXISTS embeddings (
    id SERIAL PRIMARY KEY,
    chunk_id INTEGER REFERENCES chunks(id) ON DELETE CASCADE,
    embedding vector(1536), -- OpenAI ada-002 produces 1536-dimensional vectors
    model VARCHAR(100) DEFAULT 'text-embedding-ada-002',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index for cosine similarity search
CREATE INDEX idx_embeddings_vector ON embeddings USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

CREATE INDEX idx_embeddings_chunk_id ON embeddings(chunk_id);

-- Tags table: skills and topics extracted from content
CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50), -- 'skill', 'topic', 'technology', etc.
    aliases TEXT[], -- Alternative names or spellings
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tags_name ON tags(name);
CREATE INDEX idx_tags_category ON tags(category);

-- Chunk tags: many-to-many relationship
CREATE TABLE IF NOT EXISTS chunk_tags (
    chunk_id INTEGER REFERENCES chunks(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    confidence FLOAT DEFAULT 1.0,
    PRIMARY KEY (chunk_id, tag_id)
);

CREATE INDEX idx_chunk_tags_chunk_id ON chunk_tags(chunk_id);
CREATE INDEX idx_chunk_tags_tag_id ON chunk_tags(tag_id);

-- Queries table: log user queries for analytics
CREATE TABLE IF NOT EXISTS queries (
    id SERIAL PRIMARY KEY,
    query_text TEXT NOT NULL,
    query_type VARCHAR(50), -- 'search', 'answer', 'study-plan', 'interview-prep'
    results_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE INDEX idx_queries_created_at ON queries(created_at);
CREATE INDEX idx_queries_query_type ON queries(query_type);

-- Study plans table: generated study plans for users
CREATE TABLE IF NOT EXISTS study_plans (
    id SERIAL PRIMARY KEY,
    role_id VARCHAR(100),
    current_skills TEXT[],
    weeks INTEGER,
    plan_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_study_plans_role_id ON study_plans(role_id);

-- Functions for updating timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_documents_updated_at BEFORE UPDATE ON documents
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- View: Full chunk information with document metadata
CREATE OR REPLACE VIEW chunk_full_view AS
SELECT 
    c.id as chunk_id,
    c.content,
    c.heading,
    c.heading_level,
    c.chunk_index,
    d.id as document_id,
    d.source_path,
    d.course_id,
    d.module_id,
    d.file_type,
    e.id as embedding_id,
    e.embedding,
    d.metadata as document_metadata,
    c.metadata as chunk_metadata,
    array_agg(t.name) FILTER (WHERE t.name IS NOT NULL) as tags
FROM chunks c
JOIN documents d ON c.document_id = d.id
LEFT JOIN embeddings e ON e.chunk_id = c.id
LEFT JOIN chunk_tags ct ON ct.chunk_id = c.id
LEFT JOIN tags t ON ct.tag_id = t.id
GROUP BY c.id, d.id, e.id, e.embedding;

-- Function for semantic search
CREATE OR REPLACE FUNCTION search_similar_chunks(
    query_embedding vector(1536),
    match_threshold FLOAT DEFAULT 0.5,
    match_count INT DEFAULT 10
)
RETURNS TABLE (
    chunk_id INTEGER,
    document_id INTEGER,
    source_path VARCHAR,
    heading TEXT,
    content TEXT,
    similarity FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        cfv.chunk_id,
        cfv.document_id,
        cfv.source_path,
        cfv.heading,
        cfv.content,
        1 - (cfv.embedding <=> query_embedding) as similarity
    FROM chunk_full_view cfv
    WHERE cfv.embedding IS NOT NULL
        AND 1 - (cfv.embedding <=> query_embedding) > match_threshold
    ORDER BY cfv.embedding <=> query_embedding
    LIMIT match_count;
END;
$$ LANGUAGE plpgsql;

COMMENT ON TABLE documents IS 'Stores metadata about source KB documents';
COMMENT ON TABLE chunks IS 'Text chunks extracted from documents with heading context';
COMMENT ON TABLE embeddings IS 'Vector embeddings for semantic search';
COMMENT ON TABLE tags IS 'Skills, topics, and technologies extracted from content';
COMMENT ON TABLE chunk_tags IS 'Many-to-many relationship between chunks and tags';
COMMENT ON TABLE queries IS 'Log of user queries for analytics';
COMMENT ON TABLE study_plans IS 'Generated study plans for users';

COMMENT ON FUNCTION search_similar_chunks IS 'Semantic search using cosine similarity on embeddings';
