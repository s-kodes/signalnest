import pytest
from pydantic import ValidationError

from backend.models import Article

def test_article_accepts_valid_data():
    article = Article(
        title="Understanding Kubernetes Operators",
        url="https://example.com/kubernetes-operators",
        source="The New Stack",
        topics=["Kubernetes", "SRE"],
    )

    assert article.title == "Understanding Kubernetes Operators"
    assert str(article.url) == "https://example.com/kubernetes-operators"
    assert article.topics == ["Kubernetes", "SRE"]
    assert article.published_at is None
    assert article.summary is None
    assert article.is_paywalled is None


def test_article_rejects_invalid_url():
    with pytest.raises(ValidationError):
        Article(
            title="Article with invalid URL",
            url="not-a-valid-url",
            source="Example",
        )
