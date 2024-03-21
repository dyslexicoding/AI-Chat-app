from audio_player import AudioManager
from obs_websockets import OBSWebsocketsManager
from azure_text_to_speech import AzureTTSManager
import random
class TTSManager:
    azuretts_manager = AzureTTSManager()
    audio_manager = AudioManager()
    obswebsockets_manager = OBSWebsocketsManager()

    user1_voice_name = "en-US-JaneNeural"
    user1_voice_style = "random"
    user2_voice_name = "en-US-TonyNeural"
    user2_voice_style = "random"
    user3_voice_name = "en-US-DavisNeural"
    user3_voice_style = "random"


    def __init__(self):
        file_path = self.azuretts_manager.text_to_audio("voice Chat App is now running!") # plays when started
        self.audio_manager.play_audio(file_path, True, True, True)

    def update_voice_name(self, user_number, voice_name):
        if user_number == "1":
            self.user1_voice_name = voice_name
        elif user_number == "2":
            self.user2_voice_name = voice_name
        elif user_number == "3":
            self.user3_voice_name = voice_name
        
    def update_voice_style(self, user_number, voice_style):
        if user_number == "1":
            self.user1_voice_style = voice_style
        elif user_number == "2":
            self.user2_voice_style = voice_style
        elif user_number == "3":
            self.user3_voice_style = voice_style

    def text_to_audio(self, text, user_number):
        if user_number == "1":
            voice_name = self.user1_voice_name
            voice_style = self.user1_voice_style
        elif user_number == "2":
            voice_name = self.user2_voice_name
            voice_style = self.user2_voice_style
        elif user_number == "3":
            voice_name = self.user3_voice_name
            voice_style = self.user3_voice_style

        tts_file = self.azuretts_manager.text_to_audio(text, voice_name, voice_style)
        # TODO make this for the Pawns
        # OPTIONAL: Use OBS Websockets to enable the Move plugin filter
        AltPicture1 = False
        AltPicture2 = False
        AltPicture3 = False
        
        if user_number == "1":
            if random.randint(0,50) == 50:
                AltPicture1 = True
                self.obswebsockets_manager.set_filter_visibility("live", "pawn1_alt_in", True)
            else:
                self.obswebsockets_manager.set_filter_visibility("live", "pawn1_in", True)
        elif user_number == "2":
            if random.randint(0,50) == 50:
                AltPicture2 = True
                self.obswebsockets_manager.set_filter_visibility("live", "pawn2_alt_in", True)
            else:
                self.obswebsockets_manager.set_filter_visibility("live", "pawn2_in", True)
        elif user_number == "3":
            if random.randint(0,50) == 50:
                AltPicture3 = True
                self.obswebsockets_manager.set_filter_visibility("live", "pawn3_alt_in", True)
            else:
                self.obswebsockets_manager.set_filter_visibility("live", "pawn3_in", True)
        
        self.audio_manager.play_audio(tts_file, True, True, True)

        if user_number == "1":
            if AltPicture1 == True:
                AltPicture1 = False
                self.obswebsockets_manager.set_filter_visibility("live", "pawn1_alt_out", True)
            else:
                self.obswebsockets_manager.set_filter_visibility("live", "pawn1_out", True)
        elif user_number == "2":
            if AltPicture2 == True:
                AltPicture2 = False
                self.obswebsockets_manager.set_filter_visibility("live", "pawn2_alt_out", True)
            else:
                self.obswebsockets_manager.set_filter_visibility("live", "pawn2_out", True)
        elif user_number == "3":
            if AltPicture3 == True:
                AltPicture3 = False
                self.obswebsockets_manager.set_filter_visibility("live", "pawn3_alt_out", True)
            else:
                self.obswebsockets_manager.set_filter_visibility("live", "pawn3_out", True)
