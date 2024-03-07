from endstone.command import Command, CommandSender
from endstone.plugin import Plugin
from endstone_example.python_command import PythonCommand, PythonCommandExecutor
from endstone_example.test_command import TestCommand


class ExamplePlugin(Plugin):
    def on_load(self) -> None:
        self.logger.info("on_load is called!")

    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")
        # note we pass in PythonCommand instead of PythonCommand() - use a class rather than an instance
        self.register_command(PythonCommand).executor = PythonCommandExecutor()
        self.register_command(TestCommand)

    def on_disable(self) -> None:
        self.logger.info("on_disable is called!")

    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        # You can also handle commands here instead of setting an executor in on_enable if you prefer
        if not args:
            sender.send_message(f"/{command.name} is executed from Python!")
        else:
            sender.send_message(f"/{command.name} is executed from Python with argument {args[0]}!")

        return True