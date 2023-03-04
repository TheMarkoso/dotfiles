--[[
  ██╗███╗   ██╗██╗████████╗██╗     ██╗   ██╗ █████╗
  ██║████╗  ██║██║╚══██╔══╝██║     ██║   ██║██╔══██╗
  ██║██╔██╗ ██║██║   ██║   ██║     ██║   ██║███████║
  ██║██║╚██╗██║██║   ██║   ██║     ██║   ██║██╔══██║
  ██║██║ ╚████║██║   ██║██╗███████╗╚██████╔╝██║  ██║
  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
Neovim init file
--]]

----------------------------------------------------
-- Import Lua modules
----------------------------------------------------

require('settings')							      -- settings
require('keymaps')							      -- keymaps
require('plugins/packer')				      -- plugin manager


require('plugins/treesitter')		      -- treesitter interface
require('plugins/tokyo_night')        -- colo Theme
require('plugins/color_highlight')    -- color highlights
require('plugins/cokeline')           -- bufferline
require('plugins/autopairs')          -- autopairs
require('plugins/blackline')          -- blackline
require('plugins/neotree')            -- Neo tree
require('plugins/feline')             -- Lualine
require('plugins/term')               -- Term

local lsp = require('lsp-zero')
lsp.preset('recommended')
lsp.nvim_workspace()
lsp.setup()
