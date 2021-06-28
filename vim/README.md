# VIM Shortcuts

### NERDTREE

Use the natural Vim navigation keys **`hjkl`** to navigate the files.

**`o`** open the file in a new buffer or open/close directory.

**`t`** open the file in a new tab.

**`i`** open the file in a new horizontal split.

**`s`** open the file in a new vertical split.

**`p`** go to parent directory.

**`r`** refresh the current directory.

**`m`** launch NERDTree menu inside Vim.

**`shift + i`** show hidden files.

### Replace

**`:s/foo/bar/g`** find each occurrence of 'foo' (in the current line only), and replace it with 'bar'.

**`:%s/foo/bar/g`** find each occurrence of 'foo' (in all lines), and replace it with 'bar'.

**`:%s/foo/bar/gc`** change each 'foo' to 'bar', but ask for confirmation first.

**`:%s/\<foo\>/bar/gc`** change only whole words exactly matching 'foo' to 'bar'; ask for confirmation.

**`:%s/foo/bar/gci`** change each 'foo' (case insensitive due to the `i` flag) to 'bar'; ask for confirmation.`:%s/foo\c/bar/gc` is the same because `\c` makes the search case insensitive.This may be wanted after using `:set noignorecase` to make searches case sensitive (the default).

**`:%s/foo/bar/gcI`** change each 'foo' (case sensitive due to the `I` flag) to 'bar'; ask for confirmation.`:%s/foo\C/bar/gc` is the same because `\C` makes the search case sensitive.This may be wanted after using `:set ignorecase` to make searches case insensitive.

**`:%s/\v(f\w\w)/\1bar`** to use regex capture groups with vim, use \v to start substitute and `\1`, `\2`... for each group number.`

The `g` flag means global – each occurrence in the line is changed, rather than just the first

**`Ctrl+r`** shortcut in vimrc after selecting in visual mode

### Copy / Paste / Delete

**`p`** Paste

**`y`** Copy or **`yy`** for entire line

**`d`** Cut / Delete, **`dd`** for entire line, **`daw`** for current word

Use visual mode for copying > one word

**`v}`** or  **`v{`** to copy to end/begiining of parapaph

**`"*p`** **`"*y`** accesses clipboard buffer to copy/paste from clipboard

### Search

**`/foo`** to find foo - **`n`** for next occurrence and **`N`** for previous occurrence.

**`*`** to find next occurrence of word under cursor

**`#`** to find previous occurrence of word under cursor

### Normal-mode to Insert

**`i`** Insert at cursor

**`o`** Insert on next line

**`A`** Insert / append to end of line

### Screen-splitting

**`CTRL+w, v`** Opens a new vertical split

**`CTRL+w, c`** Closes a window but keeps the buffer

**`CTRL+w, o`** Closes other windows, keeps the active window only

**`CTRL+w, right arrow`**: Moves the cursor to the window on the right

**`CTRL+w, r`** Moves the current window to the right

**`CTRL+w, =`** Makes all splits equal size

### Exiting

**`:x`** equivalent to `:wq` but only writes to disk if changes have been made. While the contents would be the same, `:wq` will change modification time whereas `:x` won't if changes have not been made.

### Navigation

**`g`** Go to beginning of file

**`G`** Go to end of file

**`:[num]`** Go to line number `[num]`

**`{`** Go to start of paragraph

**`}`** Go to end of paragraph

#### Natural Text Editing

Select Natural Text Editing from iTerm2's profile in preferences

Insert / Normal Mode moving:
fn = CMD (moves entire sentence across)
shift = option (moves word across)

Normal Mode editing:

**`w`** end of word

**`b`** beginning word

**`$`** end of line

**`^`** begining of line

### Insert Mode Edit Commands

```
CTRL-O h  move cursor left
CTRL-O l  move cursor right
CTRL-O j  move cursor down
CTRL-O k  move cursor up
CTRL-W    delete word to the left of cursor
CTRL-O D  delete everything to the right of cursor
CTRL-U    delete everything to the left of cursor
CTRL-H    backspace/delete
CTRL-J    insert newline (easier than reaching for the return key)
CTRL-T    indent current line
CTRL-D    un-indent current line
```

### Jedi-Vim

Add `set splitbelow` to .vimrc for showing quickfix list below

**`ctrl+C`** completion
**`\g`** goto assignment
**`\d`** goto function
**`\r`** renaming
**`\n`** usages

### Multi-line Edit

**`>`** and **`<`** for indents (use visual mode to select multiple lines)

Text Edit:
1. **`Ctrl+v`** to enter visual block mode
2. **`Shift+i`** to insert
3. **`esc esc`** to make changes

### Vim-Diff

vimdiff filea fileb

git difftool --tool=vimdiff --no-prompt filea

### Wrap

:set wrap nowrap (off)

:set wrap linebreak (on)

**`\w`** shortcut in vimrc

### Random

**`gc{motion}`** Comment

Insert mode calculation <C-r>={exp}

Upper / lowercause: **`gU{motion}`** or **`gu{motion}`**

Normal mode replace char **`r`**

Replace line with -: **`Vr-`**

Move: Select and `:` followed by "m{address}" - **`:'<,'>m$`** where `:'<,'>` is visual selection

Shell: `:shell` launches puts vim in background `:!{cmd}` for one-off commands. `read !{cmd}` to paste stdout to vim cursor.

Split horizontal `:sp` or vertical `:vsp`

Cycle between windows `C-w w` or `C-w {hjkl}`. Close/keep only `C-w c/o`.
