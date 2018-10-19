# 该方法用来截图的,文件命名imgname
from WaiQin.src.wq_import_export.config.read_config import ReadConfigFile


def get_window_img(self, logger, img_name, num):
    readConfig = ReadConfigFile()
    img_path = readConfig.img_path + img_name + str(num) + '.jpg'
    print(img_path)
    try:
        self.driver.save_screenshot(img_path)
        logger.info("已经截图并保存在:/Screenshot目录下")
    except NameError as e:
        logger.error("保存截图失败！%s" % e)
        self.get_window_img()
