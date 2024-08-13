return {
  'MeanderingProgrammer/markdown.nvim',
  main = "render-markdown",
  opts = {},
  name = 'render-markdown', -- Solo si tienes otro plugin llamado markdown.nvim
  dependencies = { 
    'nvim-treesitter/nvim-treesitter',  -- Asegúrate de que nvim-treesitter esté instalado
    'nvim-tree/nvim-web-devicons'  -- Dependencia opcional si usas la suite de mini.nvim
    -- Puedes descomentar y usar otras dependencias si es necesario
    -- 'echasnovski/mini.icons', -- Si usas mini-icons en lugar de mini.nvim
    -- 'nvim-tree/nvim-web-devicons', -- Si prefieres nvim-web-devicons
  },
}
