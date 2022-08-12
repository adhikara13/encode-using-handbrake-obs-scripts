import obspython as obs
import datetime
import pathlib
import subprocess

class Data:
    Handbrake = None
    OutputDir = None
    OutputConvert = None

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
  
                subprocess.run(fr'{cli} --preset "Very Fast 720p30" -i "{thefile}" -o "{convert}\{namefile}.m4v"')
                
                
        return True

def script_update(settings):
    Data.Handbrake = obs.obs_data_get_string(settings,"handbrake")
    Data.OutputDir = obs.obs_data_get_string(settings,"outputdir")
    Data.OutputConvert = obs.obs_data_get_string(settings,"outputconvert")

def script_description():
    return ("Choose the HandbrakeCLI.exe file and folder where recordings are saved."
        " When recording is stopped, the most-recent file"
            " will be converted and shown selected in Windows Explorer."
            " \n\nBy: adhkr (credit to: dustractor)")

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
    return props

obs.obs_frontend_add_event_callback(frontend_event_handler)