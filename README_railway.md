# Trash Girl KOMOJU Webhook Server (Railway対応)

## デプロイ方法（Railway）

1. このプロジェクトをGitHubにアップロード
2. [https://railway.app](https://railway.app) にログイン
3. 「New Project」→ GitHub連携 → このリポジトリを選択
4. `Environment` に以下を設定：
   - `KOMOJU_SECRET_KEY=sk_test_xxxxxx`
5. `firebase-service-account.json` をプロジェクトにアップロード（セキュアに）
6. 自動デプロイ後、Webhook URLをKOMOJU管理画面に登録：

