# Contributor Guide

Thank you for your interest in contributing to the Career AI Assistant project! This guide will help you get started.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Knowledge Base Contributions](#knowledge-base-contributions)
- [Code Contributions](#code-contributions)
- [Documentation](#documentation)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

Be respectful, professional, and constructive. This is an educational project - help others learn.

## Getting Started

### Prerequisites
- Git basics (Course 4 material)
- Node.js 18+ for API/Worker/Web
- PostgreSQL knowledge for database work
- Markdown skills for KB contributions

### Development Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/Epetaway/xrwvm-fullstack_developer_capstone.git
   ```
4. Create a branch for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Areas Needing Help
- **Knowledge Base Content**: Populate courses 1-11, 13-15 with educational content
- **API Implementation**: Build Express.js RAG endpoints
- **Worker Implementation**: Create KB ingestion and embedding pipeline
- **Web UI**: Build Next.js interface
- **Tests**: Add unit, integration, and E2E tests
- **Documentation**: Improve guides and architecture docs
- **Bug Fixes**: Fix issues in existing code

### Finding Issues
- Check [GitHub Issues](https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/issues)
- Look for `good-first-issue` label for beginners
- Ask maintainers if you're unsure where to start

## Knowledge Base Contributions

### Before You Start
1. Read `kb/STYLE_GUIDE.md` thoroughly
2. Choose a course/module to contribute to
3. Research the topic using official documentation
4. **DO NOT** copy from Coursera or other copyrighted sources

### Content Guidelines

#### ✅ Do
- Paraphrase and explain in your own words
- Use examples and code snippets from official docs
- Cite sources in `references.md`
- Include practical, hands-on content
- Connect concepts to career applications
- Test code examples before adding them
- Use clear, teaching-focused language

#### ❌ Don't
- Copy/paste from Coursera course materials
- Plagiarize from blogs or tutorials
- Use copyrighted images without permission
- Invent facts or make unsupported claims
- Add content without understanding it

### KB File Structure
```markdown
# Module Title

## Objectives
- Clear learning objectives

## Key Concepts
### Concept Name
Explanation with examples

## Tools & Commands
```bash
command --example
```

## Code Snippets
```python
# Working, tested code example
```

## Common Pitfalls
Common mistakes and solutions

## Mini Quiz
5 questions with detailed answers

## Practice Task
Hands-on exercise

## Career Notes
How this applies to jobs
```

### Adding New Content
1. Navigate to the course module file
2. Fill in the template sections
3. Ensure all code examples work
4. Add relevant citations to `references.md`
5. Test that links work
6. Submit PR with clear description

### Example Good Contribution
```markdown
## Key Concepts

### React Components

React components are reusable pieces of UI that can be composed together to build complex interfaces. There are two types:

**Functional Components** (modern approach):
```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

**Class Components** (legacy):
```javascript
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

Functional components with hooks are preferred in modern React development because they're simpler and more flexible.

**Source**: [React Documentation - Components](https://react.dev/learn/your-first-component)
```

### Example Bad Contribution
```markdown
❌ Components are the building blocks of React. They are like functions that return HTML. You can make class components or function components.
```
(Too vague, no examples, no citations, unclear)

## Code Contributions

### API/Worker/Web Development

#### Setup
```bash
# API
cd apps/api
npm install
cp .env.example .env
# Edit .env with your settings
npm run dev

# Worker
cd apps/worker
npm install
cp .env.example .env
npm run dev

# Web
cd apps/web
npm install
cp .env.example .env
npm run dev
```

#### Code Style
- Use TypeScript for type safety
- Follow existing code patterns
- Use ESLint and Prettier
- Write self-documenting code with clear names
- Add comments for complex logic only

#### Architecture Decisions
- Follow patterns in `docs/architecture.md`
- Discuss major changes in issues first
- Keep services decoupled
- Use dependency injection
- Handle errors gracefully

### Adding New Features

1. **Plan**: Open an issue describing the feature
2. **Design**: Get feedback on approach
3. **Implement**: Write code following style guide
4. **Test**: Add unit and integration tests
5. **Document**: Update relevant docs
6. **Submit**: Create pull request

### File Naming Conventions
- Use kebab-case for files: `user-service.ts`
- Use PascalCase for classes: `class UserService`
- Use camelCase for functions: `function getUserById()`

## Documentation

### Types of Documentation
- **README**: High-level project overview and quick start
- **Architecture**: System design and component interaction
- **API Docs**: Endpoint specifications
- **Guides**: How-to guides for specific tasks
- **Reference**: KB content for learning

### Writing Good Documentation
- Start with the goal/outcome
- Provide context and examples
- Use diagrams when helpful
- Keep it up-to-date with code changes
- Test documentation by following it yourself

## Testing

### Test Requirements
- New features must include tests
- Bug fixes should include regression tests
- Maintain or improve code coverage

### Running Tests
```bash
# API tests
cd apps/api
npm test

# Worker tests
cd apps/worker
npm test

# Web tests
cd apps/web
npm test

# All tests
npm run test:all
```

### Test Structure
```typescript
describe('UserService', () => {
  describe('getUserById', () => {
    it('should return user when found', async () => {
      // Arrange
      const userId = '123';
      
      // Act
      const user = await userService.getUserById(userId);
      
      // Assert
      expect(user).toBeDefined();
      expect(user.id).toBe(userId);
    });
    
    it('should throw error when not found', async () => {
      // Arrange
      const userId = 'nonexistent';
      
      // Act & Assert
      await expect(userService.getUserById(userId))
        .rejects
        .toThrow('User not found');
    });
  });
});
```

## Pull Request Process

### Before Submitting
- [ ] Code follows project style guide
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] Branch is up-to-date with main

### PR Description Template
```markdown
## Description
Brief summary of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactoring

## Related Issues
Fixes #123

## Changes Made
- Change 1
- Change 2

## Testing
How to test the changes

## Screenshots (if applicable)
Before/after or UI changes

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Code reviewed locally
- [ ] No breaking changes (or documented)
```

### Review Process
1. Maintainers will review within 3-5 days
2. Address feedback in new commits
3. Once approved, PR will be merged
4. Your contribution will be acknowledged!

### Commit Messages
Use conventional commits format:
```
feat: add study plan generation endpoint
fix: resolve CORS issue in API
docs: update architecture diagram
test: add tests for vector search
refactor: simplify chunk processing logic
```

## Community

### Getting Help
- Ask questions in GitHub Discussions
- Check existing issues and PRs
- Read documentation thoroughly first
- Be patient and respectful

### Becoming a Maintainer
Active contributors who demonstrate:
- Quality contributions
- Code review participation
- Community helpfulness
- Long-term commitment

May be invited to join as maintainers.

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

## Attribution

Contributors will be acknowledged in:
- README.md contributors section
- Git commit history
- Release notes

Thank you for contributing to making this resource better for everyone! 🎓
