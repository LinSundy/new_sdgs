def init_view(module):
    @module.route('/a/')
    def a():
        return '你好'
