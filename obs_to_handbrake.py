import obspython as obs
import datetime
import pathlib
import subprocess

presets = ['Very Fast 1080p30', 'Very Fast 720p30', 'Very Fast 576p25', 'Very Fast 480p30', 'Fast 1080p30', 'Fast 720p30', 'Fast 576p25', 'Fast 480p30', 'HQ 1080p30 Surround', 'HQ 720p30 Surround', 'HQ 576p25 Surround', 'HQ 480p30 Surround', 'Super HQ 1080p30 Surround', 'Super HQ 720p30 Surround', 'Super HQ 576p25 Surround', 'Super HQ 480p30 Surround', 'Discord Nitro Large 3-6 Minutes 1080p30', 'Discord Nitro Medium 5-10 Minutes 720p30', 'Discord Nitro Small 10-20 Minutes 480p30', 'Discord Small 2 Minutes 360p30', 'Discord Tiny 5 Minutes 240p30', 'Gmail Large 3 Minutes 720p30', 'Gmail Medium 5 Minutes 480p30', 'Gmail Small 10 Minutes 288p30', 'Vimeo YouTube HQ 2160p60 4K', 'Vimeo YouTube HQ 1440p60 2.5K', 'Vimeo YouTube HQ 1080p60', 'Vimeo YouTube HQ 720p60', 'Vimeo YouTube 720p30', 'Amazon Fire 2160p60 4K HEVC Surround', 'Amazon Fire 1080p30 Surround', 'Amazon Fire 720p30', 'Android 1080p30', 'Android 720p30', 'Android 576p25', 'Android 480p30', 'Apple 2160p60 4K HEVC Surround', 'Apple 1080p60 Surround', 'Apple 1080p30 Surround', 'Apple 720p30 Surround', 'Apple 540p30 Surround', 'Chromecast 2160p60 4K HEVC Surround', 'Chromecast 1080p60 Surround', 'Chromecast 1080p30 Surround', 'Playstation 2160p60 4K Surround', 'Playstation 1080p30 Surround', 'Playstation 720p30', 'Playstation 540p30', 'Roku 2160p60 4K HEVC Surround', 'Roku 1080p30 Surround', 'Roku 720p30 Surround', 'Roku 576p25', 'Roku 480p30', 'Xbox 1080p30 Surround', 'H.265 MKV 2160p60', 'H.265 MKV 1080p30', 'H.265 MKV 720p30', 'H.265 MKV 576p25', 'H.265 MKV 480p30', 'H.264 MKV 2160p60', 'H.264 MKV 1080p30', 'H.264 MKV 720p30', 'H.264 MKV 576p25', 'H.264 MKV 480p30', 'VP9 MKV 2160p60', 'VP9 MKV 1080p30', 'VP9 MKV 720p30', 'VP9 MKV 576p25', 'VP9 MKV 480p30', 'VP8 MKV 1080p30', 'VP8 MKV 720p30', 'VP8 MKV 576p25', 'VP8 MKV 480p30', 'H.265 NVENC 2160p 4K', 'H.265 NVENC 1080p', 'H.265 QSV 2160p 4K', 'H.265 QSV 1080p', 'H.265 VCN 2160p 4K', 'H.265 VCN 1080p', 'H.265 MF 2160p 4K', 'H.265 MF 1080p', 'Production Max', 'Production Standard', 'Production Proxy 1080p', 'Production Proxy 540p', 'CLI Default']

class Data:
    Handbrake = None
    OutputDir = None
    OutputConvert = None
    PresetList = None

def frontend_event_handler(data):
    if data == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        path = pathlib.Path(Data.OutputDir)
        if path.exists():
            now_ts = datetime.datetime.now()
            dirlist = path.iterdir()
            t = None
            for t in sorted([(
                    ( now_ts-datetime.datetime.fromtimestamp(_.stat().st_mtime)
                     ).total_seconds(),_) for _ in dirlist]):
                break
            if t:
                ign,thefile = t
                cli = pathlib.Path(Data.Handbrake)
                convert = pathlib.Path(Data.OutputConvert)
                namefile = pathlib.Path(thefile).stem
                subprocess.run(fr'explorer /select,{thefile}')
                cmd = fr'{cli} --preset "{Data.PresetList}" -i "{thefile}" -o "{convert}\{namefile}.m4v"'
                subprocess.Popen(["powershell", "-Command", cmd])
                
        return True

def script_load(settings):
    Data.Handbrake = obs.obs_data_get_string(settings,"handbrake")
    Data.OutputDir = obs.obs_data_get_string(settings,"outputdir")
    Data.OutputConvert = obs.obs_data_get_string(settings,"outputconvert")
    Data.PresetList = obs.obs_data_get_string(settings,"presetlist")

def script_update(settings):
    Data.Handbrake = obs.obs_data_get_string(settings,"handbrake")
    Data.OutputDir = obs.obs_data_get_string(settings,"outputdir")
    Data.OutputConvert = obs.obs_data_get_string(settings,"outputconvert")
    Data.PresetList = obs.obs_data_get_string(settings,"presetlist")
    

def script_description():
    return ('<center><h2> OBS to HandBrakeCLI </h2></center><center><h4>If you run into any problems, open an issue on <a href="https://github.com/adhikara13/encode-using-handbrake-obs-scripts">GitHub</a></h4></center>' 
        "Choose the HandbrakeCLI.exe file and folder where recordings are saved."
        " When recording is stopped, the most-recent file"
        " will be converted and shown selected in Windows Explorer."
        "<h6>By: adhkr (credit to: dustractor) </h6>")

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_path(
        props, "handbrake", "HandbrakeCLI", obs.OBS_PATH_FILE,
        "HandbrakeCLI (*.exe)", str(pathlib.Path.home()))
    obs.obs_properties_add_path(
        props, "outputdir", "Recordings folder", obs.OBS_PATH_DIRECTORY,
        None, str(pathlib.Path.home()))
    obs.obs_properties_add_path(
        props, "outputconvert", "Output folder", obs.OBS_PATH_DIRECTORY,
        None, str(pathlib.Path.home()))
    preset_list = obs.obs_properties_add_list(
        props, "presetlist", "Presets", obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING)
    for all in presets: 
        obs.obs_property_list_add_string(preset_list, all, all)
    return props

obs.obs_frontend_add_event_callback(frontend_event_handler)
