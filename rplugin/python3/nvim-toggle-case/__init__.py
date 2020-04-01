import neovim

@neovim.plugin
class NvimCMakeProj(object):

    def __init__(self, nvim):
        self.__nvim = nvim

    def echo(self, msg):
        self.nvim.command("echo '" + msg + "'")

    @neovim.command('CMakeReload')
    def cmake_reload(self):
        self.echo("test")
