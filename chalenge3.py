# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:29:48 2018

@author: Administrator
"""
class Args:#命令行解析类
    def __init__(self,args):
        self.args=args
    def get_args(self,arg):#输入命令行关键符号，获取参数对应的文件路径
        try:
            value=self.args[self.args.index(arg)+1]
        except(ValueError,IndexError):
            value=None
        if value is None:
            raise ArgError('not found arg %s'%arg)
        return value
class SheBaoConfig: #社保配置文件类
    def __init__(self,file):
        self.file=file
    def __parse_config(self):#解析配置文件，获取文件参数
        rate=0
        jishu_low=0
        jishu_high=0
        with open(self.file) as f:
            for line in f:
                key,value=line.split('=')
                key=key.strip()
                try:
                    value=float(value.strip())
                except ValueError:
                    continue
                if key=='JiShuL':
                    jishu_low=value
                elif key=='JiShuH':
                    jishu_high=value
                else:
                    rate+=value
        return jishu_low,jishu_high,rate
class EmployeeData:#员工文件类
    def __init_(self,file):
        self.file=file
    def __iter__(self):
        self.__file=open(self.file)
        for line in self.__file:
            employee_id,gongzi=line.split(',')
            yield int(employee_id),int(gongzi)
        self.__file.close()
class Exporter:#导出文件类
    def __init__(self,file,append=False):
        if append:
            mode='a'
        else:
            mode='w'
        self.__file=open(file,mode)
    def export(self,item):
        line=','.join(item)+'\n'
        self.__file.write(line)
    def close(self):
        self.__file.close()
class Calculator:#计算个人税
    “““
    计算方法：
    应纳税所得额=工资-保险费-起征点（3500）
    应纳税额=应纳税所得额*税率-速算扣除数
    最终工资=工资-保险-应纳税额
    低于最低缴费标准jishu_low的时候，按照jishu_low来计算保额
    高于最高缴费标准jishu_high的时候，按照jishu_high来计算保额
    ”””
    tax_start=3500#税额起征点
    tax_table=[(80000,0.45,13505),(55000,0.35,5505),(35000,0.3,2755),(9000,0.25,1005),
               (4500,0.2,555)，(1500,0.1,105),(0,0.03,0)]#个人所得税速查表(应纳税额，税率，速查扣除数)
    def __init__(self,config):
        self.config=config
    def calculate(self,data_item):# data_item 是员工数据，元组形式传过来（101,5000）
        employee_id,gongzi=data_item
        #计算社保金额
        if gongzi<self.jishu_low:
            shebao=self.jishu_low*self.config.rate
        elif gongzi>self.jishu_high:
            shebao=self.jishu_high*self.config.rate
        else:
            shebao=gongzi*self.config.rate
        #计算工资减去社保
        left_gongzi=gongzi-shebao
        #计算应纳所得额
        tax_gongzi=lest_gongzi-self.tax_start
        if tax_gongzi<0: #如果应纳税所得额小于0，就不用缴纳个人所得税
            tax=0
        else:
            for item in self.tax_table:
                if tax_gongzi>item[0]:
                    tax=tax_gongzi*item[1]-item[2]
                    break
        #最终工资=工资-社保-个人所得税
        last_gongzi=left_gongzi-tax
        return str(employee_id),str(gongzi),':.2f'.format(shebao),':.2f'.format(tax),':.2f'.format(last_gongzi)
        
            
if __name=='__main__':
    args=Args(sys.args[1:])#得到命令行的列表
    file_value=SheBaoConfig(args.get_args('-c')) #得到社保配置文件路径
    config=__parse_config(file_value)#得到社保配置内容
    self.employee_data=__iter__(EmployeeData(args.get_args('-d')))#行的形式得到员工数据
    self.exporter=Exporter(args.get_args('-o'))#行的形式导出数据到文件
    self.calculator=Calculator(config)
    #按行处理员工数据
    for item in self.employee_data:
        item=self.calculator.calculator(item)
        self.exporter.export(item)
    self.exporter.close()

