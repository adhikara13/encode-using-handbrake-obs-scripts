import obspython as obs
import datetime
import pathlib
import subprocess

presets = ["Very Fast 1080p30", "Very Fast 720p30"]

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