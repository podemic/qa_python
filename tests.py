import pytest


class TestBooksCollector:
    @pytest.mark.parametrize('name', ['Речные заводи', 'Щегол'])
    def test_add_new_book(self, collector, name):  # проверка добавления книжек с правильной длиной названия
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'ОченьИнтереснаяКнигаДляЛюбителейДлинныхСл'])
    def test_add_new_book_with_wrong_len_(self, collector, name):  # проверка добавления книжки с неправильной длиной названия
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_book_was_added_only_once(self, collector):  # проверяю, что книга добавлена 1 раз
        book_name = 'Щегол'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre', [('Речные заводи', 'Фантастика'), ('Щегол', 'Ужасы')])
    def test_setting_book_genre(self, collector, name, genre):  # проверяю установку жанра
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # проверка получения жанра книги по имени
    def test_get_book_genre(self, collector):
        collector.add_new_book('Речные заводи')
        collector.set_book_genre('Речные заводи', 'Фантастика')
        assert collector.get_book_genre('Речные заводи') == 'Фантастика'

    def test_books_with_specific_genre(self, collector):
        collector.add_new_book('Чебурашка')
        collector.add_new_book('Колобок')
        collector.set_book_genre("Чебурашка", "Фантастика")
        collector.set_book_genre("Колобок", "Фантастика")
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert "Чебурашка" in fantasy_books and "Колобок" in fantasy_books

    def test_get_books_genre(self, collector):
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Фантастика')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Колобок': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Колобок')
        collector.add_new_book('Приключения Сантехника Илюши')
        collector.set_book_genre('Колобок', 'Фантастика')
        collector.set_book_genre('Приключения Сантехника Илюши', 'Фантастика')
        books_for_children = collector.get_books_for_children()
        assert 'Колобок' in books_for_children and 'Приключения Сантехника Илюши' in books_for_children

    @pytest.mark.parametrize('name', ['Речные заводи', 'Щегол'])
    def test_add_book_in_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Колобок")
        collector.add_book_in_favorites('Колобок')
        collector.delete_book_from_favorites('Колобок')
        assert 'Колобок' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Эгоистичный ген')
        collector.add_new_book('Слепой Часовщик')
        collector.add_book_in_favorites('Эгоистичный ген')
        collector.add_book_in_favorites('Слепой Часовщик')
        favorites = collector.get_list_of_favorites_books()
        assert 'Эгоистичный ген' in favorites and 'Слепой Часовщик' in favorites





















