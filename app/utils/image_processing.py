import os
from flask import request, redirect
from werkzeug.utils import secure_filename
from config import Configuration


def allowed_file(filename):
    """
    Return True if the extension of the image is an allowed_extension
    """
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in Configuration.allowed_extension:
        return True
    else:
        return False


def valid_image(image):
    """
    Checks the name and the extension of the image
    """
    if image.filename == "":
        return False
    if not allowed_file(image.filename):
        return False

    return True


def uploads_folder():
    """
    Return the path of the uploads folder
    """
    img_folder = Configuration.UPLOAD_FOLDER
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    return img_folder


def image_processing(image):
    """
    Return the filename and the path of the uploaded image
    """

    filename = secure_filename(image.filename)
    img_folder = uploads_folder()

    image.save(os.path.join(img_folder, filename))
    image.close()

    return filename, img_folder
