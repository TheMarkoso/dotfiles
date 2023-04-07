-----------------------------------------------------------
-- Plugin manager configuration file
-----------------------------------------------------------

-- Plugin manager: packer.nvim
-- https://github.com/wbthomason/packer.nvim


local fn = vim.fn
local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
end

return require('packer').startup(function(use)
  -- My plugins here
  -- use 'foo1/bar1.nvim'
  -- use 'foo2/bar2.nvim'

	-- Automatically set up your configuration after clonning packer.nvim
	-- Put this at the after all plugins

  -- sqls
  use 'nanotee/sqls.nvim'

  -- ToggleTem
  use {"akinsho/toggleterm.nvim", tag = '*', config = function()
    require("toggleterm").setup()
  end}


  -- Neo tree
  use {
  "nvim-neo-tree/neo-tree.nvim",
    branch = "v2.x",
    requires = { 
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
    }
  }

	use 'wbthomason/packer.nvim'

	-- treesitter interface
	use 'nvim-treesitter/nvim-treesitter'

  -- colorscheme
  use 'folke/tokyonight.nvim'
  use 'navarasu/onedark.nvim'
  
  -- Feline
  use 'feline-nvim/feline.nvim'

  -- color highlights
  use 'brenoprata10/nvim-highlight-colors'

  -- CokeLine
  use({
    'noib3/nvim-cokeline',
    requires = 'kyazdani42/nvim-web-devicons', -- If you want devicons
  })
 

  -- Autopairs
  use {
	"windwp/nvim-autopairs",
    config = function() require("nvim-autopairs").setup {} end
  }

  -- Highlighting ident spaces
  use "lukas-reineke/indent-blankline.nvim"

  use {
    'VonHeikemen/lsp-zero.nvim',
    requires = {
      -- Soporte LSP
      {'neovim/nvim-lspconfig'},
      {'williamboman/mason.nvim'},
      {'williamboman/mason-lspconfig.nvim'},

      -- Autocompletado
      {'hrsh7th/nvim-cmp'},
      {'hrsh7th/cmp-buffer'},
      {'hrsh7th/cmp-path'},
      {'saadparwaiz1/cmp_luasnip'},
      {'hrsh7th/cmp-nvim-lsp'},
      {'hrsh7th/cmp-nvim-lua'},

      --  Snippets
      {'L3MON4D3/LuaSnip'},
      {'rafamadriz/friendly-snippets'},
    }
  }

end)
