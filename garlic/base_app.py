import logging
from typing import Any, Callable, List, Optional

import anyio
from anyio import Event


class BaseApp:
    def __init__(self) -> None:
        self._stop_event: Optional[Event] = None
        self._on_startup_calling: List[Callable[..., Any]] = []
        self._after_startup_calling: List[Callable[..., Any]] = []
        self._on_shutdown_calling: List[Callable[..., Any]] = []
        self._after_shutdown_calling: List[Callable[..., Any]] = []

    async def run(self, log_level: int = logging.INFO) -> None:
        self._init_async_cycle()
        async with anyio.create_task_group() as tg:
            tg.start_soon(self._start, log_level)
            await self._stop(log_level)
            tg.cancel_scope.cancel()

    def _init_async_cycle(self) -> None:
        if self._stop_event is None:
            self._stop_event = anyio.Event()

    async def _start(self, log_level: int = logging.INFO) -> None:
        self._log(log_level, f"{self.__class__.__name__} app starting...")
        await self._startup()
        self._log(
            log_level,
            f"{self.__class__.__name__} app started successfully! To exit press CTRL+C",
        )

    async def _stop(self, log_level: int = logging.INFO) -> None:
        assert self._stop_event, "You should call `_init_async_cycle` first"
        await self._stop_event.wait()
        self._log(log_level, f"{self.__class__.__name__} app shutting down...")
        await self._shutdown()
        self._log(log_level, f"{self.__class__.__name__} app shut down gracefully.")

    async def _startup(self) -> None:
        for func in self._on_startup_calling:
            await func()

    async def _shutdown(self) -> None:
        for func in self._on_shutdown_calling:
            await func()

    def _log(self, log_level: int, message: str) -> None:
        logging.log(log_level, message)
