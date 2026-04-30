from src.router.auth import router as AuthRouter
from src.router.promotions import router as PromotionsRouter
from src.router.user import router as UserRouter
from src.router.workspace import router as WorkspaceRouter

all_router = [AuthRouter, PromotionsRouter, UserRouter, WorkspaceRouter]


