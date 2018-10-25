# coding=utf-8
import time
from WaiQin.src.wq_add_field.service.add_field import AddField


class Add_Module_Field(object):
    def __init__(self, driver, logger, config):
        self.driver = driver
        self.logger = logger
        self.config = config

    def add_module_field(self):
        lenth = (len(self.config.Fun_Id) - 1) // 2
        modules = self.config.Fun_Id.split('-', lenth)
        for module in modules:
            fun_id = module
            try:

                # 跳转到对应模块添加字段的页面
                url = self.driver.current_url
                url2 = url.split('fun_id')[0] + 'fun_id=' + fun_id + '&part_id=0'  # split切割
                self.driver.get(url2)
                self.logger.debug('跳转到对应模块添加字段的页面')

                # 获取当前模块的模块名
                module_name = self.driver.find_element_by_xpath('//*[@id="content"]/ul/li/a').text

                # 实例化添加字段方法
                add = AddField(self.driver, self.config)
                self.logger.debug('实例化添加字段方法')
                self.logger.debug('开始添加字段')
                time.sleep(4)
                # 开始添加字段，可以将不需要添加的字段注释掉
                add.add_common_field('input', self.config.Input_Message)
                self.logger.debug('添加单行字段')

                add.add_common_field('textarea', self.config.TextareaMessage)
                self.logger.debug('添加多行字段')

                add.add_common_field('number', self.config.NumberMessage)
                self.logger.debug('添加数字字段')

                add.add_common_field('tel', self.config.TelMessage)
                self.logger.debug('添加电话字段')

                add.add_common_field('price', self.config.PriceMessage)
                self.logger.debug('添加金额字段')

                add.add_select_field('select', self.config.SelectMessage, self.config.Select1Message,
                                     self.config.Select2Message)
                self.logger.debug('添加单选-同级字段')

                add.add_select_field('multiselect', self.config.MultiselectMessage, self.config.MultiselectMessage1,
                                     self.config.MultiselectMessage2)
                self.logger.debug('添加多选-同级字段')

                # add.add_special_select_field('select', self.config.SpecialselectMessage)
                # self.logger.debug('添加单选-多级字段')
                #
                # add.add_special_select_field('multiselect', self.config.SpecialmultselectMessage)
                # self.logger.debug('添加多选-多级字段')

                add.add_common_field('date', self.config.DateMessage)
                self.logger.debug('添加日期字段')

                add.add_common_field('datetime', self.config.DatetimeMessage)
                self.logger.debug('添加时间字段')

                add.add_common_field('time_range', self.config.Time_rangeMessage)
                self.logger.debug('添加时间起止字段')

                add.add_common_field('pic', self.config.PicMessage)
                self.logger.debug('添加照片字段')

                add.add_common_field('pic_and_textarea', self.config.Pic_and_textareaMessage)
                self.logger.debug('添加照片+多行文本字段')

                add.add_common_field('line', self.config.LineMessage)
                self.logger.debug('添加标题分隔线字段')

                add.add_common_field('location', self.config.LocationMessage)
                self.logger.debug('添加自动获取位置字段')

                self.logger.info(module_name + '添加成功')
            except Exception as e:
                self.logger.info(module_name + '添加失败', format(e))
