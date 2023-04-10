require('nvim-treesitter.configs').setup({
	highlight ={
		enable = true,
	},
	ensure_installed = {
		'python',
		'html',
		'css',
		'lua',
		'bash',
		'javascript',
	},	
})
