import argparse
import obsws_python as obs

def switch_scene(ip, port, password, scene_name):
    cl = obs.ReqClient(host=ip, port=port, password=password, timeout=3)
    cl.set_current_program_scene(scene_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Switch to a named scene in OBS.")
    parser.add_argument("--ip", type=str, required=True, help="IP address of the OBS instance.")
    parser.add_argument("--port", type=int, required=True, help="Port of the OBS WebSocket server.")
    parser.add_argument("--password", type=str, required=True, help="Password for the OBS WebSocket server.")
    parser.add_argument("--scene", type=str, required=True, help="Name of the scene to switch to.")

    args = parser.parse_args()

    # Execute the main function
    switch_scene(args.ip, args.port, args.password, args.scene)