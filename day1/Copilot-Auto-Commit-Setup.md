# 🔄 Auto-Commit Setup for GitHub Copilot Training

## Overview

Setting up automatic commits helps track every change made during GitHub Copilot exercises, making it easy to revert to previous states and understand the progression of development.

## 🚀 Recommended Approaches

### 1. **VS Code Extension: GitDoc (Recommended)**

**Best for**: Real-time automatic commits on every save

```vscode-extensions
vsls-contrib.gitdoc
```

**Setup:**
1. Install GitDoc extension
2. Open Command Palette (`Cmd+Shift+P`)
3. Run `GitDoc: Enable`
4. Configure auto-commit settings

**Benefits:**
- Commits automatically on save
- Works seamlessly with GitHub Copilot
- Maintains detailed commit history
- Easy to enable/disable per project

### 2. **VS Code Extension: Git Automator**

**Best for**: Automated commit messages and workflow

```vscode-extensions
ivangabriele.vscode-git-add-and-commit
```

**Features:**
- Custom commit message templates
- Keyboard shortcuts for quick commits
- Workflow automation

### 3. **AI-Powered Commit Messages**

**Best for**: Intelligent commit message generation

```vscode-extensions
michaelcurrin.auto-commit-msg,sitoi.ai-commit
```

**Features:**
- Auto-generates meaningful commit messages
- Analyzes file changes for context
- Conventional commit format support

## 🛠️ Manual Git Hooks Setup

### Pre-Commit Hook for Training Sessions

Create a custom pre-commit hook that automatically stages and commits Copilot-related changes:

```bash
# Create pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

# Auto-commit training changes
if [ -f ".copilot-training-mode" ]; then
    echo "🤖 Copilot Training Mode: Auto-committing changes"
    
    # Add all changes
    git add .
    
    # Create commit with timestamp
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    git commit -m "🤖 Copilot Training Progress - $TIMESTAMP" --no-verify
fi
EOF

# Make executable
chmod +x .git/hooks/pre-commit
```

**To enable training mode:**
```bash
touch .copilot-training-mode
```

**To disable training mode:**
```bash
rm .copilot-training-mode
```

## 📝 VS Code Settings for Auto-Save + Auto-Commit

Add these settings to your workspace or user settings:

```json
{
    // Auto-save files for faster commits
    "files.autoSave": "onFocusChange",
    "files.autoSaveDelay": 1000,
    
    // Git settings
    "git.autofetch": true,
    "git.autoStash": true,
    "git.enableCommitSigning": false,
    
    // GitDoc specific settings (if using GitDoc extension)
    "gitdoc.enabled": true,
    "gitdoc.commitValidationLevel": "none",
    "gitdoc.commitMessageFormat": "🤖 Training: {filename} - {now}",
    "gitdoc.pullOnOpen": false,
    "gitdoc.pushOnSave": false,
    "gitdoc.commitOnSave": true
}
```

## 🎯 Training-Specific Commit Strategy

### Commit Message Conventions

Use consistent prefixes to track different types of changes:

- `🤖 Copilot:` - Changes made with Copilot assistance
- `✏️ Manual:` - Manual code changes
- `🧪 Exercise:` - Specific exercise completions
- `🔧 Setup:` - Configuration and setup changes
- `🐛 Fix:` - Bug fixes during exercises
- `📚 Docs:` - Documentation updates

### Example Workflow Script

Create a training helper script:

```bash
#!/bin/bash
# save as: copilot-commit.sh

EXERCISE_NAME="$1"
DESCRIPTION="$2"

if [ -z "$EXERCISE_NAME" ]; then
    echo "Usage: ./copilot-commit.sh <exercise-name> [description]"
    exit 1
fi

# Add all changes
git add .

# Create detailed commit message
TIMESTAMP=$(date "+%H:%M:%S")
if [ -n "$DESCRIPTION" ]; then
    COMMIT_MSG="🤖 Exercise: $EXERCISE_NAME - $DESCRIPTION [$TIMESTAMP]"
else
    COMMIT_MSG="🤖 Exercise: $EXERCISE_NAME completed [$TIMESTAMP]"
fi

# Commit with message
git commit -m "$COMMIT_MSG"

echo "✅ Committed: $COMMIT_MSG"
```

**Usage:**
```bash
./copilot-commit.sh "interface-basics" "Completed keyboard shortcuts practice"
./copilot-commit.sh "entity-creation" "Added User entity with JPA annotations"
```

## 🔍 Commit History Navigation

### Useful Git Commands for Training

```bash
# View training session commits
git log --oneline --grep="🤖"

# View commits from last hour
git log --since="1 hour ago" --oneline

# View commits for specific file
git log --oneline -- src/main/java/com/taskmanager/app/entity/User.java

# Create checkpoint tags
git tag -a "checkpoint-$(date +%Y%m%d-%H%M)" -m "Training checkpoint"

# Quick revert to previous commit
git reset --hard HEAD~1

# View changes in last commit
git show HEAD
```

### VS Code Git Timeline

Use VS Code's built-in Git Timeline feature:
1. Open Source Control panel (`Ctrl+Shift+G`)
2. Enable Timeline view in Explorer
3. See file-by-file commit history
4. Right-click commits to revert changes

## 🚦 Quick Setup for Instructors

### One-Command Setup

Create an instructor setup script:

```bash
#!/bin/bash
# save as: setup-auto-commit.sh

echo "🤖 Setting up auto-commit for Copilot training..."

# Install GitDoc extension
code --install-extension vsls-contrib.gitdoc

# Create workspace settings
mkdir -p .vscode
cat > .vscode/settings.json << 'EOF'
{
    "files.autoSave": "onFocusChange",
    "gitdoc.enabled": true,
    "gitdoc.commitMessageFormat": "🤖 Training: {now}",
    "gitdoc.commitOnSave": true,
    "gitdoc.pushOnSave": false
}
EOF

# Create training mode marker
touch .copilot-training-mode

# Initial commit
git add .
git commit -m "🚀 Training session started with auto-commit enabled"

echo "✅ Auto-commit setup complete!"
echo "💡 Changes will now auto-commit on save"
echo "🔧 To disable: Remove .copilot-training-mode file"
```

Make executable and run:
```bash
chmod +x setup-auto-commit.sh
./setup-auto-commit.sh
```

## ⚠️ Best Practices

### Do's:
- ✅ Use descriptive commit messages with emojis
- ✅ Enable auto-commit only during training sessions
- ✅ Create checkpoint tags at major milestones  
- ✅ Review commit history regularly
- ✅ Use consistent message formatting

### Don'ts:
- ❌ Auto-commit sensitive information
- ❌ Leave auto-commit enabled for production code
- ❌ Commit incomplete or broken code frequently
- ❌ Forget to disable auto-commit after training
- ❌ Auto-push to shared repositories without review

## 🔄 Reverting Changes

### Quick Revert Options:

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert specific file to previous version
git checkout HEAD~1 -- path/to/file.java

# Interactive revert (choose commits)
git rebase -i HEAD~10
```

### VS Code Revert:
1. Open Source Control panel
2. Right-click on commit in timeline
3. Select "Revert Changes in Commit"
4. Or use "Reset to Commit" for harder reset

This setup ensures every Copilot-assisted change is tracked and easily reversible! 🎯