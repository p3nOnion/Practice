from django.contrib import admin
from .models import Writing, Speaking, PracticeS, PracticeW

# Tạo một lớp con của admin.ModelAdmin cho model Writing
class WritingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'problem', 'solution', 'count', 'user')  # Hiển thị các trường trên trang quản trị
    list_filter = ('type',)  # Thêm bộ lọc cho trường 'type'
    search_fields = ('problem', 'solution')  # Tìm kiếm dựa trên các trường 'problem' và 'solution'

# Đăng ký model Writing với tùy chỉnh của nó
admin.site.register(Writing, WritingAdmin)

# Tạo một lớp con của admin.ModelAdmin cho model Speaking
class SpeakingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'problem', 'solution', 'count', 'user')  # Hiển thị các trường trên trang quản trị
    list_filter = ('type',)  # Thêm bộ lọc cho trường 'type'
    search_fields = ('problem', 'solution')  # Tìm kiếm dựa trên các trường 'problem' và 'solution'

# Đăng ký model Speaking với tùy chỉnh của nó
admin.site.register(Speaking, SpeakingAdmin)

admin.site.register(PracticeS)
admin.site.register(PracticeW)
