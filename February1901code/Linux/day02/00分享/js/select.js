var province = $("#province"), city = $("#city"), town = $("#town");
for(var i = 0; i < provinceList.length; i++) {
	addEle(province, provinceList[i].name);
}

function addEle(ele, value) {  // 往下拉式列表添加省/市/县元素
	var optionStr = "";
	optionStr = "<option value=" + value + ">" + value + "</option>";
	ele.append(optionStr);
}

function removeEle(ele) {  // 清空市/县元素（包括请选择“请选择”的选项）
	ele.find("option").remove();
	var optionStar = "<option value=" + "请选择" + ">" + "请选择" + "</option>";
	ele.append(optionStar);  // 清空所有选项后，把“请选择”重新添加
}
var provinceText, cityText, cityItem;
province.on("change", function() {  // 当下拉框中的值发生改变时，触发“change”事件
	provinceText = $(this).val();  // 选中省，然后替换掉原来选中的text
	$.each(provinceList, function(i, item) {  // provinceList即item
		// 把省列表中的市遍历出来，并分配一个下标
		if(provinceText == item.name) {
			cityItem = i;  // 记录省所对应的下标
//			return cityItem
		}
	});
	removeEle(city);  // 调用删除函数，把之前选择中的省所有的市清除
	removeEle(town);  // 调用删除函数，把之前选择中的省所有的县清除
	$.each(provinceList[cityItem].cityList, function(i, item) {  // 
		addEle(city, item.name);
	})
});
city.on("change", function() {
	cityText = $(this).val();
	removeEle(town);
	$.each(provinceList, function(i, item) {
		if(provinceText == item.name) {
			cityItem = i;
//			return cityItem
		}
	});
	$.each(provinceList[cityItem].cityList, function(i, item) {
		if(cityText == item.name) {
			for(var n = 0; n < item.areaList.length; n++) {
				addEle(town, item.areaList[n]);
			}
		}
	});
});