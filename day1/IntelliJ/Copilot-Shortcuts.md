# GitHub Copilot — IntelliJ Keyboard Shortcuts (macOS & Windows)

This file lists common and recommended keyboard shortcuts for using GitHub Copilot inside JetBrains IntelliJ IDEA. Exact defaults can vary by Copilot plugin version, JetBrains IDE release, and your active keymap. Use the "How to verify / change" section to confirm or customize these shortcuts in your environment.

✅ Quick tip: Use "Find Action" to run any Copilot action without a keybinding: macOS: ⌘⇧A (Cmd+Shift+A) — Windows/Linux: Ctrl+Shift+A

## Recommended shortcuts (examples)

Note: the table below shows recommended (and commonly used) keybindings. Marked as "Recommended" because defaults may differ; verify in your Keymap and remap if you prefer.

| Action / Command                                | macOS (Recommended)      | Windows/Linux (Recommended) |
|-------------------------------------------------|---------------------------|------------------------------|
| Accept inline suggestion                        | Tab or →                 | Tab or →                    |
| Accept suggestion and move to next              | ⌘↩ (Cmd+Enter) *(optional)* | Ctrl+Enter *(optional)*     |
| Dismiss/Hide suggestion                         | Esc                      | Esc                         |
| See next suggestion (when multiple available)   | ⌥] (Option + ])          | Alt + ]                     |
| See previous suggestion                         | ⌥[ (Option + [)          | Alt + [                     |
| Open Copilot Chat / Focus Chat window           | ⌃⌘C (Ctrl+Cmd+C) *(example)* | Ctrl+Alt+C *(example)*      |
| Toggle inline suggestions on/off                | ⌃⌥I (Ctrl+Option+I) *(example)* | Ctrl+Alt+I *(example)*      |
| Show Copilot tool window / panel                | ⌘6 (Cmd+6) *(example)*   | Ctrl+6 *(example)*          |
| Explain selection / Ask Copilot about selection | ⌃⌘E (Ctrl+Cmd+E) *(example)* | Ctrl+Alt+E *(example)*      |
| Generate tests (Copilot-assisted)               | ⌥⌘T (Option+Cmd+T) *(example)* | Alt+Ctrl+T *(example)*      |

A few notes on the table above:
- "Accept inline suggestion" is commonly bound to Tab or the Right Arrow key in many editors/IDE keymaps. If Tab is used for indentation in your keymap, choose a different binding.
- Actions marked "*(example)*" are suggested mappings that avoid colliding with common IntelliJ defaults; they are not guaranteed defaults for the plugin — please verify in your Keymap.

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

- If an action doesn't appear in the Keymap search, confirm the GitHub Copilot plugin is installed and enabled: Preferences → Plugins → search for "GitHub Copilot".
- If inline suggestions don't appear, check: Preferences → GitHub Copilot (or the plugin settings) → ensure inline suggestions are enabled for the current file type.
- Some Copilot features (chat, explain, test generation) may require a paid Copilot or Copilot Chat subscription — check your account and plugin notices.


