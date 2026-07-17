import re


class PhishingDetector:


    suspicious_words=[
        "urgent",
        "password",
        "verify account",
        "payment"
    ]


    def scan(self,email):

        score=0

        for word in self.suspicious_words:
            if word in email.lower():
                score+=20


        return {
            "threat_score":score,
            "danger":score>50
        }


detector=PhishingDetector()