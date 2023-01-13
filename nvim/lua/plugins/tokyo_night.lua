require("tokyonight").setup({
  style = "night",
  styles = {
    comments = { italic = true },
    keywords = { italic = true },
    functions = {},
    variables = {},
    sidebars = "dark",
  },
  sidebars = { "qf", "terminal", "packer"},
})


vim.cmd[[colorscheme tokyonight]]
