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

### Copy / Paste / Delete

**`p`** Paste

**`y`** Copy or **`yy`** for entire line

**`d`** Cut / Delete, **`dd`** for entire line, **`daw`** for current word

Use visual mode for copying > one word

**`v}`** or  **`v{`** to copy to end/begiining of parapaph

### Search

**`/foo`** to find foo - **`n`** for next occurrence and **`N`** for previous occurrence.

**`*`** to find next occurrence of word under cursor

**`#`** to find previous occurrence of word under cursor

### Normal-mode to Insert

**`i`** Insert at cursor

**`o`** Insert on next line

**`a`** Insert / append to end of line

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

### Natural Scrolling in iTerm2

Mimic OS X's behavior of sending Cmd-left/right to the beginning/end of a line, add the following mappings in iTerm2:

Cmd-left to escape-sequence `[1~`
Cmd-right to escape-sequence `[4~`

To mimic OS X's behavior of sending Option-left/right to the previous/next word, add the following mappings in iTerm2:

Option-left to escape-sequence `[1;5D`
Option-right to escape-sequence `[1;5C`