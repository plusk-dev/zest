import json


def compute_material_required(width: float, height: float):
    # track
    horizontal_track = width * 2  # 2 pcs
    vertical_track = height * 2  # 2 pcs
    total_track_length = 2 * (width + height) #Unit: mm

    # framing
    horizontal_frame = (width - 9)/2  # 1 piece of horizontal frame
    handle_frame = height - 69
    total_framing_length = 6 * (horizontal_frame + handle_frame) #Unit: mm

    # glass
    glass_area = ((horizontal_frame - 105) *
                  (handle_frame - 105)) * (0.00328084**2) #Unit: sq. ft

    # mosquito net
    mosquito_area = (horizontal_frame * handle_frame) * (0.00328084**2) #Unit: sq. ft

    # glass pvc
    glass_pvc_vertical_height = handle_frame * 4 #Unit: mm
    glass_pvc_width = width * 2

    # c chanel
    c_chanel_height = handle_frame * 2 #Unit: mm
    c_chanel_width = width

    # track woolpile
    woolpile_height = handle_frame * 9  # TODO: Correction
    woolpile_width = horizontal_frame * 2  # TODO: Correction

    return {
        "Track - Top/Bottom": {
            "per_piece": round(horizontal_track / 2, 3),
            "total": horizontal_track,
            "Unit": "mm",
            "Pieces": "2"
        },
        "Track - Vertical": {
            "per_piece": round(vertical_track / 2, 3),
            "total": vertical_track ,
            "Unit": "mm",
            "Pieces": "2"
        },
        "Section - Top/Bottom" : {
            "per_piece": round(horizontal_frame / 6, 3),
            "total": horizontal_frame,
            "Unit": "mm",
            "Pieces": "6"
        },
        "Section - Handle": {
            "per_piece": round(handle_frame / 6, 3),
            "total": handle_frame,
            "Unit": "mm",
            "Pieces": "6"
        },
        "Glass": {
            "per_piece": round(glass_area/2, 3),
            "total": round(glass_area, 3),
            "Unit": "sq. ft",
            "Pieces": "2"
        },
        "Mosquito Net": {
            "per_piece": round(mosquito_area, 3),
            "total": round(mosquito_area, 3),
            "Unit": "sq. ft",
            "Pieces": "1"
        },
        "Glass PVC - Horizontal": {
            "total": glass_pvc_width,
            "Unit": "mm",
            "Pieces": "4",
            "per_piece": round(glass_pvc_width/4, 3)
        },
        "Glass PVC - Vertical": {
            "total": glass_pvc_vertical_height,
            "Unit": "mm",
            "Pieces": "4",
            "per_piece": round(glass_pvc_vertical_height/4, 3)
        },
        "C Chanel - Horizontal": {
            "Unit": "mm",
            "Pieces": "1",
            "total": c_chanel_width,
            "per_piece": c_chanel_width
        },
        "C Chanel - Vertical": {
            "Unit": "mm",
            "Pieces": "2",
            "total": c_chanel_height,
            "per_piece": round(c_chanel_height/2, 3)
        },
        "Woolpile - Horizontal": {
            "Unit": "mm",
            "Pieces": "2",
            "total":woolpile_width,
            "per_piece": round(woolpile_width / 2, 3)
        },
        "Woolpile - Vertical": {
            "Unit": "mm",
            "Pieces": "9",
            "total":woolpile_height,
            "per_piece": round(woolpile_height / 9, 3)
        },
        "Inter Lock Strip" : {
            "Pieces": "3",
            "Unit":"mm",
            "per_piece":handle_frame,
            "total":handle_frame * 3,
        },
        "Bearing" : {
            "Pieces": "6",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
        "Lock" : {
            "Pieces": "2",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
        "Aluminium Clit" : {
            "Pieces": "20",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
        "Corner Clit" : {
            "Pieces": "24",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
        "Male Female" : {
            "Pieces": "6",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
        "Long Cap" : {
            "Pieces": "3",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
        "Lock Guard" : {
            "Pieces": "3",
            "Unit":"",
            "per_piece":"-",
            "total":"-",
        },
    }


# print(json.dumps(compute_material_required(width=1524.0, height=1220.0), indent=4))
