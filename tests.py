import pytest


class TestBooksCollector:
    @pytest.mark.parametrize('name', ['Речные заводи','Щегол'])
    def test_add_new_book(self,collector,name): #проверка добавления книжек c правильной длинной названия
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name',['','ОченьИнтереснаяКнигаДляЛюбителейДлинныхСл'])
    def test_add_new_book_with_wrong_len_(self,collector,name): #проверка добавления книжки с неправильной длинной названия
        collector.add_new_book(name)
        assert name in collector.get_book_genre(name)


    def test_book_was_added_only_once(self,collector):  #проверяю, что книга добавлена 1 раз
        book_name = 'Щегол'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_book_genre()) == 1


    @pytest.mark.parametrize('name','genre',[['Речные заводи','Фантастика'],['Щегол','Ужасы']])
    def test_setting_book_genre(self,collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        assert collector.get_books_genre(name) == genre












