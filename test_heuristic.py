from app.detectors.heuristic import analyze



def test_clean_email():

    result = analyze(
        content=
        "Hi team, attached is the Q3 report.",
        subject="Report",
        sender="john@company.com"
    )

    assert result.score < 15
    assert result.ran is True



def test_payment_scam():

    result = analyze(
        content=
        """
        URGENT.
        Change bank details immediately.
        Send wire transfer today.
        """
    )

    codes = {
        x.code
        for x in result.signals
    }

    assert "URGENCY_LANGUAGE" in codes
    assert "PAYMENT_REDIRECT_REQUEST" in codes



def test_password_phishing():

    result = analyze(
        content=
        "Your account is locked. Verify your password now."
    )

    codes = {
        x.code
        for x in result.signals
    }

    assert "CREDENTIAL_HARVEST_PATTERN" in codes