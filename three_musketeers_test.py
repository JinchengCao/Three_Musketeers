import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), R)
        self.assertEqual(at((0, 4)), M)

    def test_set_board(self):
        self.assertEqual(at((0, 0)), _)
        self.assertEqual(at((1, 2)), R)
        self.assertEqual(at((1, 3)), M)

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((0, 0), string_to_location('A1'))
        self.assertEqual((2, 3), string_to_location('C4'))
        self.assertEqual((0, 4), string_to_location('A5'))
        self.assertEqual((4, 4), string_to_location('E5'))

    def test_location_to_string(self):
        self.assertEqual('A1', location_to_string((0,0)))
        self.assertEqual('C4', location_to_string((2,3)))
        self.assertEqual('A5', location_to_string((0,4)))
        self.assertEqual('E5', location_to_string((4,4)))
       
    def test_at(self):

        self.assertEqual(_, at((0, 1)))
        self.assertEqual(R, at((1, 2)))
        self.assertEqual(M, at((2, 2)))
        self.assertEqual(R, at((4, 3)))

    def test_all_locations(self):
        self.assertEqual(True, all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                          (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                          (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                          (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                          (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])

    def test_adjacent_location(self):
        self.assertEqual((1,4),adjacent_location((0,4),down))
        self.assertEqual((1,1),adjacent_location((1,2),left))                        
        self.assertEqual((0,3),adjacent_location((1,3),up))
        self.assertEqual((2,4),adjacent_location((2,3),right))                        
        
    def test_is_legal_move_by_musketeer(self):
        self.assertEqual(False, is_legal_move_by_musketeer((0, 3), down))
        self.assertEqual(True, is_legal_move_by_musketeer((2, 2), right))
        self.assertEqual(False, is_legal_move_by_musketeer((2, 2), down))
        self.assertEqual(False, is_legal_move_by_musketeer((0, 3), up))
       
    def test_is_legal_move_by_enemy(self):
        self.assertEqual(True, is_legal_move_by_enemy((3, 1), right))
        self.assertEqual(True, is_legal_move_by_enemy((4, 3), right))
        self.assertEqual(False, is_legal_move_by_enemy((2, 3), up))
        self.assertEqual(False, is_legal_move_by_enemy((2, 1), down))

    def test_is_legal_move(self):
        self.assertEqual(False, is_legal_move((2, 1), right))
        self.assertEqual(False, is_legal_move((3, 1), up))
        self.assertEqual(False, is_legal_move((3, 4), left))
        self.assertEqual(False, is_legal_move((1, 3), right))

    def test_can_move_piece_at(self):
        self.assertEqual(True, can_move_piece_at((1, 2)))
        self.assertEqual(True, can_move_piece_at((2, 2)))
        self.assertEqual(True, can_move_piece_at((4, 3)))
        self.assertEqual(False, can_move_piece_at((0, 0)))
        self.assertEqual(False, can_move_piece_at((0, 3)))
       
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere(M))
        self.assertTrue(has_some_legal_move_somewhere(R))
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ])
        self.assertFalse(has_some_legal_move_somewhere(R))
        self.assertTrue(has_some_legal_move_somewhere(M))

    def test_possible_moves_from(self):
        self.assertEqual([], possible_moves_from((0, 0)))
        self.assertEqual([], possible_moves_from((0, 3)))
        self.assertEqual([up, left], possible_moves_from((1, 2)))
        self.assertEqual([up, left,right], possible_moves_from((4, 3)))

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(True,can_move_piece_at((2,2)))
        self.assertEqual(True,can_move_piece_at((0,3)))
        self.assertEqual(False,can_move_piece_at((1,3)))
        self.assertEqual(False,can_move_piece_at((0,4)))

    def test_is_legal_location(self):
        self.assertEqual(True, is_legal_location((0, 0)))
        self.assertEqual(True, is_legal_location((4, 4)))
        self.assertEqual(False, is_legal_location((1, 5)))
        self.assertEqual(False, is_legal_location((-1, 0)))

    def test_is_within_board(self):

        self.assertEqual(True, is_within_board((2, 1), right))
        self.assertEqual(True, is_within_board((3, 1), up))
        self.assertEqual(False, is_within_board((3, 4), right))
        self.assertEqual(False, is_within_board((4, 3), down))

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                   [_, _, _, M, M],
                   [_, _, _, _, _],
                   [_, _, _, _, _],
                   [_, _, _, _, _] ] )
        self.assertEqual([((0, 3), left),
                         ((0, 3), right),((1, 4), up)], all_possible_moves_for(M))
                         #((1, 3), )
        self.assertEqual([((0, 2), down),
                         ((0, 2), left)], all_possible_moves_for(R))
                        #((0, 4), )


        
    def test_make_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ])
        make_move((1, 4),up)
        new_board = [ [_, _, R, M, M],
                       [_, _, _, M, _],
                       [_, _, _, _, _],
                       [_, _, _, _, _],
                       [_, _, _, _, _] ]
        self.assertEqual(True, get_board() == new_board)
       
    def test_choose_computer_move(self):
        x = choose_computer_move(M)
        self.assertEqual(True, is_legal_move(x[0], x[1]))
        x = choose_computer_move(R)
        self.assertEqual(True, is_legal_move(x[0], x[1]))
        set_board([ [R, R, R, _, R],
                    [R, R, R, _, R],
                    [R, R, _, M, _],
                    [R, _, _, R, R],
                    [_, M, M, _, R] ] )
        x = choose_computer_move(M)
        self.assertEqual(True, is_legal_move(x[0], x[1]))


    def test_is_enemy_win(self):
        set_board([ [_, _, R, _, R],
                    [_, _, M, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(True, is_enemy_win())
        set_board([ [_, _, R, _, R],
                    [_, _, _, M, M],
                    [_, _, _, _, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(False, is_enemy_win())              

unittest.main()
