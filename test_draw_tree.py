from draw_tree import draw_tree


def test_tree_height_3(capsys):
    draw_tree(3)
    captured = capsys.readouterr().out
    expected_output = (
        "  C  \n"
        " ACA \n"
        "RACAR\n"
    )
    assert captured == expected_output

def test_tree_height_4(capsys):
    draw_tree(4)
    captured = capsys.readouterr().out
    expected_output = (
        "   C   \n"
        "  ACA  \n"
        " RACAR \n"
        "CRACARC\n"
    )
    assert captured == expected_output

def test_tree_height_5(capsys):
    draw_tree(5)
    captured = capsys.readouterr().out
    expected_output = (
        "    C    \n"
        "   ACA   \n"
        "  RACAR  \n"
        " CRACARC \n"
        "ACRACARCA\n"
    )
    assert captured == expected_output