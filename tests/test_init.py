import contextlib
import io

from myapp import main


def test_main():
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        main()
    assert f.getvalue() == "hello hello world\n"
