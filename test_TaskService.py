import sqlite3
import unittest
from TaskService import TaskService
from TaskRepository import TaskRepository
from TaskStatusEnum import TaskStatus
from task import Task
import os


class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("todo-test.sqlite")
        self.task_repository = TaskRepository(self.db)
        self.task_repository.create_table()
        self.task_service = TaskService(self.task_repository)

    def tearDown(self):
        self.db.close()
        os.remove("todo-test.sqlite")

    def test_create_task(self):
        created = self.task_service.create_task(Task("name", "description", TaskStatus.TODO))
        self.assertIsNotNone(created.id)

    def test_remove_task(self):
        created = self.task_service.create_task(Task("name", "description", TaskStatus.TODO))
        self.task_service.remove_task(str(created.id))
        deleted = self.task_service.get_task(str(created.id))
        self.assertIsNone(deleted)

    def test_update_task(self):
        created = self.task_service.create_task(Task("name", "description", TaskStatus.TODO))
        created.set_name("new name")
        self.task_service.update_task(created)
        updated = self.task_service.get_task(str(created.id))
        self.assertEqual(created.name, updated.name)

    def test_update_task_status(self):
        created = self.task_service.create_task(Task("name", "description", TaskStatus.TODO))
        created.set_status(TaskStatus.IN_PROGRESS)
        self.task_service.update_task(created)
        updated = self.task_service.get_task(str(created.id))
        self.assertEqual(created.status, updated.status)

    def test_search_by_name(self):
        created = self.task_service.create_task(Task("name", "description", TaskStatus.TODO))
        found = self.task_service.find_by_name("m")
        self.assertEqual(1, len(found))
        self.assertEqual(created.id, found[0].id)

if __name__ == '__main__':
    unittest.main()
