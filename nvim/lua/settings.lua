local g = vim.g
local o = vim.o
local opt = vim.opt
local A = vim.api

opt.list = true
opt.listchars:append "space:⋅"
opt.listchars:append "eol:↴"
o.termguicolors = true
opt.mouse = "a"
opt.swapfile = false

-- Number of screen lines to keep above and below the cursor
o.scrolloff = 8

-- Better editor UI
o.number = true
o.relativenumber = true
o.numberwidth = 5
o.showmatch = true

-- Better editing experience
o.expandtab = true
o.smarttab = true
o.autoindent = true
o.tabstop = 2
o.wrap = true
o.shiftwidth = 2
o.breakindent = true 

-- Makes neovim and host OS clipboard play nicely with each other
o.clipboard = 'unnamedplus'

-- Case insensitive searching UNLESS /C or capital in search
o.ignorecase = true
o.smartcase = true

-- Better buffer splitting
o.splitright = true
o.splitbelow = true
