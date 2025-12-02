# GitHub Copilot — IntelliJ Keyboard Shortcuts (December 2025)

This file lists keyboard shortcuts for using GitHub Copilot in JetBrains IntelliJ IDEA. Shortcuts may vary by plugin version and your keymap configuration.

✅ **Quick tip**: Use "Find Action" to run any Copilot action: **⌘⇧A** (macOS) or **Ctrl+Shift+A** (Windows/Linux)

## Default Shortcuts

| Action                                          | macOS                    | Windows/Linux             |
|-------------------------------------------------|--------------------------|---------------------------|
| **Accept inline suggestion**                    | Tab                      | Tab                       |
| **Accept word** (partial accept)                | ⌘→ (Cmd+Right)           | Ctrl+Right                |
| **Dismiss suggestion**                          | Esc                      | Esc                       |
| **Next suggestion**                             | ⌥] (Option+])            | Alt+]                     |
| **Previous suggestion**                         | ⌥[ (Option+[)            | Alt+[                     |
| **Open Copilot Chat**                           | ⌃⏎ (Ctrl+Enter) in editor | Ctrl+Enter in editor     |
| **Inline Chat** (ask about selection)           | ⌘I (Cmd+I)               | Ctrl+I                    |
| **Show Copilot completions panel**              | ⌥\ (Option+\)            | Alt+\                     |
| **Toggle Copilot suggestions**                  | Via Settings/Preferences | Via Settings              |

## Chat-Specific Actions

| Action                                          | macOS                    | Windows/Linux             |
|-------------------------------------------------|--------------------------|---------------------------|
| **Open Chat tool window**                       | Find Action → "Copilot Chat" | Find Action → "Copilot Chat" |
| **Submit chat message**                         | ⏎ (Enter)                | Enter                     |
| **New line in chat**                            | ⇧⏎ (Shift+Enter)         | Shift+Enter               |
| **Clear chat history**                          | Click clear icon         | Click clear icon          |

## Context Menu Actions

Right-click on selected code to access:
- **Explain This** — Get explanation of selected code
- **Generate Tests** — Create unit tests for selection
- **Fix This** — Suggest fixes for issues
- **Generate Docs** — Add documentation comments

## How to verify or change Copilot shortcuts in IntelliJ

1. Open Keymap preferences:
   - macOS: IntelliJ IDEA → Preferences... → Keymap
   - Windows/Linux: File → Settings → Keymap

2. In the Keymap search box, type `Copilot` or `GitHub Copilot` to list plugin actions. Also try `Copilot Chat`, `Accept Suggestion`, `Explain Code`, etc.

3. To assign or change a shortcut:
   - Right-click the action → Add Keyboard Shortcut → press the desired key combo → OK.
   - If the key combo conflicts with an existing binding, IntelliJ will warn you; you can decide to remove or reassign the old binding.

4. Quick-run an action without binding: Press Find Action and type the action name:
   - macOS: ⌘⇧A (Cmd+Shift+A)
   - Windows/Linux: Ctrl+Shift+A

## Helpful tips and best practices

- Use non-conflicting modifiers: On macOS prefer combining Cmd (⌘) with Ctrl (⌃) or Option (⌥) for plugin actions to avoid colliding with editing shortcuts.
- Keep accept = Tab if you want the most frictionless inline experience; otherwise pick a dedicated combo for explicit acceptance.
- If you frequently use Copilot Chat, bind a single easy combo (e.g., Ctrl+Alt+C on Windows, Ctrl+Cmd+C on macOS) to open the chat quickly.
- Export your keymap (Keymap settings → gear menu) so you can reuse the shortcuts across machines.

## Troubleshooting

- **Plugin not found**: Confirm GitHub Copilot plugin is installed: Preferences → Plugins → search "GitHub Copilot"
- **No suggestions appearing**: Check Preferences → GitHub Copilot → ensure suggestions are enabled for your file type
- **Chat not working**: Verify you're signed in to GitHub and have an active Copilot subscription (Individual, Business, or Enterprise)
- **Shortcuts not working**: Check for keymap conflicts in Preferences → Keymap → search "Copilot"
