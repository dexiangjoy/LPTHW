# -*- coding: utf-8 -*-
cars = 100
space_in_a_car = 4.0 #作者在这里问为什么用4.0而不用4 ，说人不能用小数3.1个，用3.1可能代表多出来的空间
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #空车数是车子数减去司机数
cars_driven = drivers #司机全部用来开车
carpool_capacity = cars_driven * space_in_a_car #总承载量等于每辆车的承载量乘以可用的司机数
average_passengers_per_car = passengers / cars_driven
#average_passengers_per_car = car_pool_capacity / passenger  这行的car_pool 多了一个_


print "There are", cars, "cars avaiable."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
