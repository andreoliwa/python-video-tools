from click.testing import CliRunner

from vidsub.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == ""
    assert result.exit_code == 0
