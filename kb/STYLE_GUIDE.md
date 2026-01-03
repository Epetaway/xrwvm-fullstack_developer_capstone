# Knowledge Base Style Guide

## Purpose
This knowledge base (KB) documents the IBM Full Stack Cloud Developer Coursera certificate program. The KB serves as the foundation for the Career AI Assistant's RAG (Retrieval-Augmented Generation) engine.

## Core Principles

### 1. No Plagiarism
- **Never copy-paste** Coursera transcripts, course materials, or copyrighted content verbatim
- **Always paraphrase** and summarize in your own words
- When documenting technical concepts, explain them from first principles
- Use official documentation links in `references.md` files

### 2. Citation-First Approach
- Every KB file must be **citeable** by the RAG engine
- Include clear section headings (`#`, `##`, `###`) for precise citation
- File paths serve as primary citation identifiers
- Format: `kb/course-XX-name/modules/module-YY.md#heading-name`

### 3. Deterministic Organization
- Follow the **exact** folder and file naming conventions specified
- Use kebab-case for all folder and file names (e.g., `full-stack-application-development`)
- Number courses sequentially: `course-01`, `course-02`, etc.
- Number modules sequentially: `module-01.md`, `module-02.md`, etc.

## File Naming Rules

### Course Folders
Format: `course-[NN]-[course-name-kebab-case]/`
- NN is a zero-padded two-digit number (01, 02, ... 15)
- Course name uses kebab-case (all lowercase, hyphens between words)
- Examples:
  - `course-01-introduction-to-software-engineering/`
  - `course-12-full-stack-application-development-capstone-project/`

### Module Files
Format: `module-[NN].md`
- NN is a zero-padded two-digit number (01, 02, ... 05)
- Examples:
  - `modules/module-01.md`
  - `modules/module-05.md`

### Cheatsheet Files
Fixed names in `cheatsheets/` subdirectory:
- `commands.md` - CLI commands, tool usage
- `patterns.md` - Design patterns, common solutions
- `interview.md` - Interview questions and answers

### Lab Files
Format: `lab-index.md` in `labs/` subdirectory
- Single index file linking to all lab notes and exercises

### References
Format: `references.md` in course root
- Links to official documentation
- Academic papers or textbooks
- Community resources
- **Never** link to copyrighted course materials directly

## Content Structure

### Every Course Folder Must Contain
```
course-NN-name/
├── README.md           # Overview, learning outcomes, glossary
├── modules/
│   ├── module-01.md
│   ├── module-02.md
│   ├── module-03.md
│   ├── module-04.md
│   └── module-05.md
├── cheatsheets/
│   ├── commands.md
│   ├── patterns.md
│   └── interview.md
├── labs/
│   └── lab-index.md
└── references.md
```

### Every Module File Must Include

```markdown
# Module [N]: [Title]

## Objectives
- Bullet list of learning objectives
- What students will be able to do after this module

## Key Concepts
- Fundamental ideas and theories
- Core terminology with definitions

## Tools & Commands
- Software tools introduced
- CLI commands with syntax and examples
- Configuration files

## Code Snippets
- Practical code examples (if applicable)
- Annotated with explanations
- Language-specific best practices

## Common Pitfalls
- Typical mistakes beginners make
- How to avoid or fix them
- Debugging strategies

## Mini Quiz
1. Question 1?
   - **Answer:** Explanation

2. Question 2?
   - **Answer:** Explanation

(Include 5 questions minimum)

## Practice Task
- Hands-on exercise description
- Expected outcomes
- Hints and guidance

## Career Notes
- How this module's content applies to real-world jobs
- Relevant job titles and roles
- Industry expectations
```

### Course README Template

```markdown
# Course [N]: [Full Course Title]

## Overview
Brief description of the course purpose and scope.

## Learning Outcomes
By completing this course, you will be able to:
- Outcome 1
- Outcome 2
- Outcome 3

## Course Modules
1. [Module 1 Title](modules/module-01.md)
2. [Module 2 Title](modules/module-02.md)
3. [Module 3 Title](modules/module-03.md)
4. [Module 4 Title](modules/module-04.md)
5. [Module 5 Title](modules/module-05.md)

## Glossary
- **Term 1**: Definition
- **Term 2**: Definition

## Practical Exercises
See [Labs Index](labs/lab-index.md) for hands-on exercises.

## Cheatsheets
- [Commands](cheatsheets/commands.md)
- [Patterns](cheatsheets/patterns.md)
- [Interview Questions](cheatsheets/interview.md)

## References
See [references.md](references.md) for external resources.
```

## Writing Guidelines

### Summaries
- Be concise but complete
- Focus on practical application
- Include context: why does this matter?
- Use examples to illustrate concepts

### Paraphrasing
- Read the source material thoroughly
- Close the source and write from memory
- Explain as if teaching a peer
- Verify accuracy without copying phrasing

### Code Examples
- Use realistic, working code
- Include comments for clarity
- Show both correct and incorrect patterns (in Common Pitfalls)
- Prefer simple examples over complex ones

### Technical Accuracy
- Verify all commands and syntax
- Test code snippets when possible
- Link to official documentation for authoritative information
- Mark uncertain information as `TODO: Verify`

## Handling Missing Information

If you don't have enough information to document a section:

```markdown
## [Section Name]

> **TODO**: This section requires additional research and documentation.
> 
> Expected topics:
> - Topic 1
> - Topic 2
> 
> See [references.md](references.md) for potential sources.
```

**Never invent facts**. The RAG engine will return "Not found in knowledge base yet" if information is missing.

## Citation Format

When the RAG engine cites KB content, it uses this format:

```
Source: kb/course-05-developing-front-end-apps-with-react/modules/module-02.md#Component-Lifecycle
```

Therefore:
- Use descriptive heading names (not generic "Section 1")
- Keep heading names stable (they become part of the citation)
- Use proper Markdown heading hierarchy (`#`, `##`, `###`)

## Quality Checklist

Before considering a course module complete:

- [ ] All required sections present
- [ ] No copy-pasted content from Coursera
- [ ] All code examples tested (if applicable)
- [ ] Mini quiz includes 5+ questions
- [ ] Practice task is actionable
- [ ] Career notes connect to real jobs
- [ ] References.md includes official docs
- [ ] File names follow conventions
- [ ] Headings are descriptive and stable

## Maintenance

- **Version control**: All KB changes go through Git
- **Review process**: Major content additions should be reviewed
- **Update policy**: Update when official documentation changes or errors are found
- **Deprecation**: Mark outdated content clearly rather than deleting

## Example: Good vs. Bad

### ❌ Bad (Copied)
> "In this module you will learn about React hooks. React hooks are functions that let you use state and other React features without writing a class."

### ✅ Good (Paraphrased)
> Hooks are functions that enable functional components to manage state and lifecycle events, which previously required class components. This modern approach simplifies component logic and improves code reusability.

---

**Remember**: This KB powers a Career AI Assistant. Every piece of content should help learners build real-world skills and prepare for software development careers.
