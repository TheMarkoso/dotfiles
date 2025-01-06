local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}
local cmd = vim.cmd


-- don't use arrow keys
map('', '<up>', '<nop>', {noremap = true})
map('', '<down>', '<nop>', {noremap = true})
map('', '<left>', '<nop>', {noremap = true})
map('', '<right>', '<nop>', {noremap = true})

-- move in insert mode
map('i', '<c-h>', '<left>', default_opts)
map('i', '<c-j>', '<down>', default_opts)
map('i', '<c-k>', '<up>', default_opts)
map('i', '<c-l>', '<right>', default_opts)

-- nvim-tree
map('n', '<c-n>', ':Neotree toggle<cr>', default_opts)       -- open/close


-- move line in normal mode
-- mover línea hacia abajo en modo normal
map('n', '<a-j>', ':m .+1<cr>==', { noremap = true, silent = true })

-- mover línea hacia arriba en modo normal
map('n', '<a-k>', ':m .-2<cr>==', { noremap = true, silent = true })

-- mover líneas hacia abajo en modo visual
map('v', '<a-j>', ":m '>+1<cr>gv=gv", { noremap = true, silent = true })

-- mover líneas hacia arriba en modo visual
map('v', '<a-k>', ":m '<-2<cr>gv=gv", { noremap = true, silent = true })

-- moverse al siguiente buffer usando tab
map('n', '<tab>', ':BufferLineCycleNext<cr>', { noremap = true, silent = true })

-- moverse al buffer anterior usando shift+tab
map('n', '<s-tab>', ':BufferLineCyclePrev<cr>', { noremap = true, silent = true })


-- Leader key mappings

-- save file
map('n', '<leader>w', ':w<CR>', default_opts)

-- Quit Neovim
--map('n', '<leader>q', ':q<CR>', default_opts)

-- Save and quit
map('n', '<leader>x', ':wq<CR>', default_opts)


-- Save and close current buffer
map('n', '<leader>q', ':w<CR>:bd<CR>', {noremap = true, silent = true})

map('n', '<c-t>', ':ToggleTerm<cr>', default_opts)       -- open/close
