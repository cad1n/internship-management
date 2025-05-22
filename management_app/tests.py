import pytest, os
from unittest.mock import patch, MagicMock
from django.http import HttpResponse
from management_app.render import Render

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

@pytest.mark.django_db
@patch("management_app.render.get_template")
@patch("management_app.render.pisa.pisaDocument")
def test_render_pdf_success(mock_pisa, mock_get_template):
    # Mock do template
    mock_template = MagicMock()
    mock_template.render.return_value = "<html><body>PDF</body></html>"
    mock_get_template.return_value = mock_template

    # Mock do pisaDocument
    mock_pdf = MagicMock()
    mock_pdf.err = False
    mock_pisa.return_value = mock_pdf

    response = Render.render("fake_template.html", {"foo": "bar"})
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response["Content-Type"] == "application/pdf"

@patch("management_app.render.get_template")
@patch("management_app.render.pisa.pisaDocument")
def test_render_pdf_error(mock_pisa, mock_get_template):
    mock_template = MagicMock()
    mock_template.render.return_value = "<html><body>PDF</body></html>"
    mock_get_template.return_value = mock_template

    mock_pdf = MagicMock()
    mock_pdf.err = True
    mock_pisa.return_value = mock_pdf

    response = Render.render("fake_template.html", {"foo": "bar"})
    assert isinstance(response, HttpResponse)
    assert response.status_code == 400
    assert b"Error Rendering PDF" in response.content
