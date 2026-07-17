class VoiceCloneDetector:


    def analyze(self,audio):

        return {
            "clone_probability":0.10,
            "result":"human"
        }


detector=VoiceCloneDetector()