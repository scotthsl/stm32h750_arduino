# GPIO映射方法
1. wiring库的API接收一个pinnumber，这个pin number 在variant目录中的文件variant.h定义，为一个宏定义。
2. variant.cpp中包含一个const PinName digitalPin[] 数组，数组中的元素是枚举值，在文件 PinNames.h中定义，这个枚举值实际包含了port索引和pin索引。digitalPin[]数组中的元素和variant.h中的宏定义是一一对应的，否则使用gpio时会出错。如假设宏定义 PA0=0，则digitalPin[0]必须等于枚举值 PA_0

# 为外设指定复用的IO引脚