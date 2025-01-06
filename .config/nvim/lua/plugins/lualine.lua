return {
  'nvim-lualine/lualine.nvim',
  lazy = false,
  config = function ()
    require('lualine').setup({
      options = {
        theme = 'tokyonight-night', -- Puedes cambiarlo por el tema que prefieras
        section_separators = '',
        component_separators = '',
      },
      sections = {
        lualine_a = {'mode'},
        lualine_b = {'branch', 'diff', 'diagnostics'},
        lualine_c = {'filename'},
        lualine_x = {'encoding', 'fileformat', 'filetype'},
        lualine_y = {'progress'},
        lualine_z = {'location'}
      },
    })
  end

}
