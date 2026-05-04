from src.router.auth import router as AuthRouter
from src.router.promotions import router as PromotionsRouter
from src.router.user import router as UserRouter
from src.router.workspace import router as WorkspaceRouter
from src.router.floor import router as FloorRouter
from src.router.resource import router as ResourceRouter

all_router = [AuthRouter, PromotionsRouter, UserRouter, WorkspaceRouter, FloorRouter, ResourceRouter]