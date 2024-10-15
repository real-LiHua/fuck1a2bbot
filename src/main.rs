use teloxide::prelude::*;
use teloxide::utils::command::BotCommands;

async fn callback(bot: Bot, msg: Message) -> ResponseResult<()> {
    println!("test");
    Ok(())
}

#[derive(BotCommands, Clone)]
#[command(rename_rule = "lowercase", parse_with = "split")]
enum Command {
    Fuck1a2b,
}

#[tokio::main]
async fn main() -> ResponseResult<()> {
    pretty_env_logger::init();
    log::info!("Starting bot...");

    let bot = Bot::from_env();
    Command::repl(bot, action).await;
    Ok(())
}

async fn action(bot: Bot, msg: Message, cmd: Command) -> ResponseResult<()> {
    match cmd {
        Command::Fuck1a2b => callback(bot, msg).await?,
    };
    Ok(())
}
