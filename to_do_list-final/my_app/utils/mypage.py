class Page:
    def __init__(self, page_num, per_page=10, max_page=7):
        self.page_num = page_num
        self.per_page = per_page
        self.max_page = max_page
        self.data_start = (self.page_num-1) * self.per_page
        self.data_end = self.page_num * self.per_page
        self.half_max_page = self.max_page // 2


    @property
    def start(self):
        data_start = (self.page_num - 1) * self.per_page
        return data_start
    @property
    def end(self):
        data_end = self.page_num * self.per_page
        return data_end

        form_obj = TaskForm()
    def page_html(self, data_name):
        total_count = data_name.objects.count()
        total_page, m = divmod(total_count, self.per_page)
        if m:
            total_page += 1
        page_start = max(self.page_num - self.half_max_page, 1)
        page_end = min(self.page_num + self.half_max_page, total_page + 1)
        html_str_list = []
        html_str_list.append('<li><a href="/about/?page={0}">首页</a></li>'.format(1))
        for i in range(page_start, page_end + 1):
            if i == self.page_num:
                tmp = '<li class="active"><a  href="/about/?page={0}">{0}</a></li>'.format(i)
            else:
                tmp = '<li><a href="/about/?page={0}">{0}</a></li>'.format(i)
            html_str_list.append(tmp)
        html_str_list.append('<li><a href="/about/?page={0}">尾页</a></li>'.format(total_page))
        html_list = "".join(html_str_list)
        former_page = max(self.page_num - 1, 1)
        next_page = min(self.page_num + 1, total_page)
        return html_list, former_page, next_page
