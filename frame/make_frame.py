from frame import frame as fr

def image_frame_insert(image, shape, name, color=(218,255,48)):
    if name[:3] != "Eye":
        if name[8:] == "Round":
            blusher = fr.Blusher("Round")
            image = blusher.frame(image, shape, color)
        elif name[8:] == "Oblong":
            blusher = fr.Blusher("Oblong")
            image = blusher.frame(image, shape, color)
        elif name[8:] == "Square":
            blusher = fr.Blusher("Square")
            image = blusher.frame(image, shape, color)
    elif name[:7] == "Eyebrow":
        if name[8:] == "Arch":
            eye = fr.EyeBrow("Arch")
            image = eye.frame(image, shape, False, (False, "round"), color)  # 파일 X
        elif name[8:] == "Straight":
            eye = fr.EyeBrow("Straight")
            image = eye.frame(image, shape, color)
    elif name[:8] == "EyeLiner":
        if name[9:] == "Up":
            eye = fr.EyeLiner("Up")
            image = eye.frame(image, shape, color)
        elif name[9:] == "Middle":
            eye = fr.EyeLiner("Middle")
            image = eye.frame(image, shape, color)
    elif name[:9] == "EyeShadow":
        eye = fr.EyeBrow("Arch")
        eye.frame(image, shape, True, color)   # 텍스트 파일만 생셩
        if name[10:] == "Middle":
            eye = fr.EyeShadow("Middle")
            image = eye.frame(image, shape, color)
        elif name[10:] == "Large":
            eye = fr.EyeShadow("Large")
            image = eye.frame(image, shape, color)
        elif name[10:] == "Small":
            eye = fr.EyeShadow("Small")
            image = eye.frame(image, shape, color)
    return image

def customize_eyebrow_frame(image, shape, name, color=(218,255,48)):
    output = image
    if name == "oblong":
        eye = fr.EyeBrow("Straight")
        output = eye.frame(image, shape, color)
    else:
        eye = fr.EyeBrow("Arch")
        if name == "square":
            output = eye.frame(image, shape, False, (True, "square"), color)
        else:
            output = eye.frame(image, shape, False, (True, "round"), color)
    return output
