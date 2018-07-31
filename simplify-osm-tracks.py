#!/usr/bin/env python
"""Analyse a GPX track file containing banned roads, and simplify."""

# Assumptions:
#   

import sys
import gpxpy

def read_and_simplify(gpx):
    """Read GPX file and eliminate unnecessary XML elements"""
    
    print("Loading GPX file...", file=sys.stderr, end="", flush=True)
    seg_dict = {}
    for track in gpx.tracks:
        track.description = ""
        for segment in track.segments:
            for point in segment.points:
                seg_dict[point.time] = [point.latitude, point.longitude, point.elevation]
    print("OK\n", file=sys.stderr, end="", flush=True)

    # create a new GPX file and populate it with all the segments in th eoriginal
    newgpx = gpxpy.gpx.GPX()

    # Create first track in our GPX:
    singletrack = gpxpy.gpx.GPXTrack()
    singletrack.name = "(highway=trunk or highway=primary) and bicycle=no"
    for track in gpx.tracks:
        for segment in track.segments:
            singletrack.segments.append(segment)

    newgpx.tracks.append(singletrack)

    print (newgpx.to_xml())
    return []



## MAIN ##
INFILE = str(sys.argv[1])
## INFILE = "FPRtP.gpx"
GPXPY = gpxpy.parse(open(INFILE))
read_and_simplify(GPXPY)

