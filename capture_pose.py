from pykinect import nui
import numpy as np

kinect = nui.Runtime()
kinect.skeleton_engine.enabled = True

def skeleton_frame_ready(frame):
    for skeleton in frame.SkeletonData:
        if skeleton.eTrackingState == nui.SkeletonTrackingState.TRACKED:
            print("Skeleton detectado:")
            for joint in skeleton.SkeletonPositions:
                print(f"  x={joint.x:.2f}, y={joint.y:.2f}, z={joint.z:.2f}")
            print("---")
            break

kinect.skeleton_frame_ready += skeleton_frame_ready

print("Kinect activo. Presioná Ctrl+C para salir...")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Finalizado.")
