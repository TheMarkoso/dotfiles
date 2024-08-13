--return {
--  "tek256/simple-dark",
--  lazy = false, -- make sure we load this during startup if it is your main colorscheme
--  priority = 1000, -- make sure to load this before all the other start plugins
--  config = function()
--    -- load the colorscheme here
--    vim.cmd([[colorscheme simple-dark]])
--  end,
--}

return {
   "tiagovla/tokyodark.nvim",
    lazy = false,
    config = function()
      vim.cmd[[colorscheme tokyodark]]
    end,
}

--return {
--   "dasupradyumna/midnight.nvim",
--    lazy = false,
--    config = function()
--      vim.cmd[[colorscheme midnight]]
--    end,
--}

--return {
--   "alexanderbluhm/black.nvim",
--    lazy = false,
--    config = function()
--      vim.cmd[[colorscheme black]]
--    end,
--}
